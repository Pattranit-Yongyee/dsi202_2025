# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Camp, UserProfile
from .forms import CampForm, UserProfileForm

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
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            profile.grade_level = form.cleaned_data['grade_level']
            profile.other_grade = form.cleaned_data['other_grade']
            profile.hobbies = form.cleaned_data['hobbies']
            profile.interests = form.cleaned_data['interests']
            profile.save()
            return redirect('home')
    else:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(initial={
            'grade_level': profile.grade_level,
            'other_grade': profile.other_grade,
            'hobbies': profile.hobbies,
            'interests': profile.interests,
        })
    return render(request, 'camps/profile.html', {'form': form, 'user': request.user})