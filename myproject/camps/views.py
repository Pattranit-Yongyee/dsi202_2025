# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Camp, StudentProfile
from .forms import CampForm, StudentProfileForm
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import date


def home(request):
    categories = {
        'health': 'สายสุขภาพ',
        'engineering': 'สายวิศวกรรม',
        'architecture': 'สายสถาปัตยกรรม',
        'language': 'สายภาษา',
        'volunteer': 'ค่ายจิตอาสา',
        'digital-it': 'ดิจิตอล ไอที',
    }

    camps_by_category = {}
    for slug, display_name in categories.items():
        camps = Camp.objects.filter(category=slug, approved=True)[:3]
        camps_by_category[slug] = {
            'display_name': display_name,
            'camps': camps
        }

    
    # ดึงค่ายที่ใกล้ปิดรับสมัคร
    close_soon_camps = Camp.objects.filter(
        approved=True,
        application_deadline__isnull=False,
        application_deadline__gte=date.today()
    ).order_by('application_deadline')[:10]

    # คำนวณวันเหลือ
    for camp in close_soon_camps:
        camp.days_left = (camp.application_deadline - date.today()).days

    return render(request, 'camps/home.html', {
        'camps_by_category': camps_by_category,
        'close_soon_camps': close_soon_camps,
    })

def category_camps(request, category_slug):
    # แสดงค่ายทั้งหมดในหมวดหมู่
    camps = Camp.objects.filter(category=category_slug, approved=True).order_by('application_deadline')
    category_name = dict(Camp.CATEGORY_CHOICES).get(category_slug, 'Unknown Category')

    return render(request, 'camps/category_camps.html', {'camps': camps, 'category_name': category_name})

def category(request, category_slug):
    # Map category slug to category name
    category_mapping = {
        'health': 'สุขภาพ',
        'engineering': 'วิศวกรรม',
        'digital-it': 'ดิจิทัลและไอที',
        'architecture': 'สถาปัตยกรรม',
        'language': 'ภาษา',
        'volunteer': 'จิตอาสา',
    }

    # Get category name for display
    category_name = category_mapping.get(category_slug, 'ไม่ทราบหมวดหมู่')

    # Get camps in the category
    camps = Camp.objects.filter(
        category=category_slug,
        approved=True,
        application_deadline__gte=timezone.now().date()
    ).order_by('application_deadline')

    return render(request, 'camps/category.html', {
        'camps': camps,
        'category_name': category_name,
        'category_slug': category_slug,
    })

def camp_detail(request, camp_id):
    # แสดงรายละเอียดค่าย
    camp = get_object_or_404(Camp, pk=camp_id)
    return render(request, 'camps/camp_detail.html', {'camp': camp})

def add_camp(request):
    if request.method == 'POST':
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            new_camp = form.save(commit=False)
            new_camp.approved = False
            new_camp.save()
            return render(request, 'camps/camp_submission_success.html')
    else:
        form = CampForm()

    return render(request, 'camps/add_camp.html', {'form': form})


@login_required
def complete_profile(request):
    try:
        profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        profile = StudentProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'บันทึกข้อมูลโปรไฟล์เรียบร้อยแล้ว')
            return redirect('profile')
    else:
        form = StudentProfileForm(instance=profile, user=request.user)

    return render(request, 'camps/complete_profile.html', {'form': form})

@login_required
def profile(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    camps = []

    if profile.hobbies or profile.interests:
        # รวม hobbies และ interests
        keywords = []
        if profile.hobbies:
            keywords.extend([h.strip().lower() for h in profile.hobbies.split(',')])
        if profile.interests:
            keywords.extend([i.strip().lower() for i in profile.interests.split(',')])

        # Map Thai category names to Camp model category values
        category_mapping = {
            'สุขภาพ': 'health',
            'วิศวกรรม': 'engineering',
            'ไอที': 'digital-it',
            'ดิจิทัล': 'digital-it',
            'สถาปัตยกรรม': 'architecture',
            'ภาษา': 'language',
            'จิตอาสา': 'volunteer',
            'วิทยาศาสตร์': 'digital-it',
            'โปรแกรมมิ่ง': 'digital-it',
            'ศิลปะ': 'architecture',
        }

        # สร้าง query สำหรับค้นหาค่าย
        filters = Q()
        for keyword in keywords:
            # จับคู่กับ category
            for thai_category, model_category in category_mapping.items():
                if thai_category in keyword:
                    filters |= Q(category=model_category)
            # จับคู่กับ title และ description
            filters |= Q(title__icontains=keyword) | Q(description__icontains=keyword)

        # ดึงค่ายที่ตรงเงื่อนไข
        camps = Camp.objects.filter(
            filters,
            approved=True,
            application_deadline__gte=timezone.now().date()
        ).distinct().order_by('application_deadline')[:15]

    # ถ้าไม่มีค่ายที่ตรงกัน แสดงค่ายทั่วไป
    if not camps:
        camps = Camp.objects.filter(
            approved=True,
            application_deadline__gte=timezone.now().date()
        ).order_by('application_deadline')[:5]  # ใช้ application_deadline แทน created_at

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudentProfileForm(instance=profile, user=request.user)

    return render(request, 'camps/profile.html', {
        'profile': profile,
        'form': form,
        'user': request.user,
        'camps': camps,
    })