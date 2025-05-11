# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Camp, StudentProfile
from .forms import CampForm, StudentProfileForm
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

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

    # We need to ensure application_deadline is a DateField in the model for proper sorting
    close_soon_camps = Camp.objects.filter(approved=True).order_by('application_deadline')[:10]

    return render(request, 'camps/home.html', {
        'camps_by_category': camps_by_category,
        'close_soon_camps': close_soon_camps,
    })

def category_camps(request, category_slug):
    # แสดงค่ายทั้งหมดในหมวดหมู่
    camps = Camp.objects.filter(category=category_slug, approved=True).order_by('application_deadline')
    category_name = dict(Camp.CATEGORY_CHOICES).get(category_slug, 'Unknown Category')

    return render(request, 'camps/category_camps.html', {'camps': camps, 'category_name': category_name})

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
        # Combine hobbies and interests, split by commas, and strip whitespace
        keywords = []
        if profile.hobbies:
            keywords.extend([h.strip() for h in profile.hobbies.split(',')])
        if profile.interests:
            keywords.extend([i.strip() for i in profile.interests.split(',')])
        
        # Map Thai category names to Camp model category values
        category_mapping = {
            'สุขภาพ': 'health',
            'วิศวกรรม': 'engineering',
            'ไอที': 'digital-it',
            'ดิจิทัล': 'digital-it',
            'สถาปัตยกรรม': 'architecture',
            'ภาษา': 'language',
            'จิตอาสา': 'volunteer',
        }
        
        # Build query for matching categories
        category_filters = Q()
        for keyword in keywords:
            for thai_category, model_category in category_mapping.items():
                if thai_category in keyword:
                    category_filters |= Q(category=model_category)
        
        # Query camps with matching categories, approved, and future deadlines
        camps = Camp.objects.filter(
            category_filters,
            approved=True,
            application_deadline__gte=timezone.now().date()
        ).order_by('application_deadline')[:15]
    
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