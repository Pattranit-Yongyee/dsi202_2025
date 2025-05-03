# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CampForm, StudentProfileForm
from .models import Camp, CampCategory, StudentProfile
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import CampForm
from .models import Camp

def homepage(request):
    categories = CampCategory.objects.all()
    approved_camps = Camp.objects.filter(status='approved').order_by('-submit')[:3]
    return render(request, 'camps/homepage.html', {'categories': categories, 'approved_camps': approved_camps})

def category_page(request, category_id):
    category = get_object_or_404(CampCategory, id=category_id)
    camps = Camp.objects.filter(category=category, status='approved')
    return render(request, 'camps/category_page.html', {'category': category, 'camps': camps})

def camp_detail(request, camp_id):
    camp = get_object_or_404(Camp, id=camp_id, status='approved')
    return render(request, 'camps/camp_detail.html', {'camp': camp})
    
@login_required
def organize_camp(request):
    if request.method == 'POST':
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            camp = form.save(commit=False)
            camp.organizer_name = request.user.username  # หรือใช้ฟิลด์อื่นจากผู้ใช้
            camp.submit = timezone.now()  # ถ้ามีการใช้ timezone
            camp.save()
            return redirect('homepage')
    else:
        form = CampForm()
    return render(request, 'camps/organize_camp.html', {'form': form})

@login_required
def profile_page(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=request.user.studentprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        profile, created = StudentProfile.objects.get_or_create(user=request.user)
        form = StudentProfileForm(instance=profile)
    return render(request, 'camps/profile.html', {'form': form})

@login_required
def search_camp(request):
    profile = request.user.studentprofile
    if request.method == 'POST':
        query = request.POST.get('query', '')
        camps = Camp.objects.filter(status='approved').filter(
            camp_name__icontains=query
        ).filter(
            candi_proper__icontains=profile.interest
        ) | Camp.objects.filter(status='approved').filter(
            typeof_camp__icontains=profile.interest
        )
    else:
        camps = Camp.objects.filter(status='approved')
    return render(request, 'camps/search_camp.html', {'camps': camps, 'profile': profile})

@login_required
def organize_camp(request):
    if request.method == 'POST':
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            camp = form.save(commit=False)
            camp.organizer_name = request.user.username  # หรือใช้ฟิลด์อื่นจากผู้ใช้
            camp.submit = timezone.now()  # ถ้ามีการใช้ timezone
            camp.save()
            return redirect('homepage')  # กลับไปหน้า homepage หลังบันทึก
    else:
        form = CampForm()
    return render(request, 'camps/organize_camp.html', {'form': form})