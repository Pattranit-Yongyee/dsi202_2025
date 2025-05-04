from django.shortcuts import render, get_object_or_404
from .models import Camp
from .forms import CampForm

def home(request):
    categories = {
        'health': 'สายสุขภาพ',
        'engineering': 'สายวิศวกรรม',
        'architecture': 'สายสถาปัตยกรรม',
        'language': 'สายภาษา',
        'volunteer': 'ค่ายจิตอาสา',
        'digital': 'ดิจิตอล/ไอที',
    }

    camps_by_category = {}
    for slug, display_name in categories.items():
        camps = Camp.objects.filter(category=slug, approved=True)[:3]  # เฉพาะค่ายที่ได้รับการอนุมัติ
        camps_by_category[slug] = {
            'display_name': display_name,
            'camps': camps
        }

    return render(request, 'camps/home.html', {'camps_by_category': camps_by_category})

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