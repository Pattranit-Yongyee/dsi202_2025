from django.shortcuts import render, get_object_or_404
from .models import Camp
from django.http import Http404

def home(request):
    categories = dict(Camp.CATEGORY_CHOICES)
    camps_by_category = {}

    for key, display_name in categories.items():
        camps = Camp.objects.filter(category=key)[:3]
        camps_by_category[display_name] = camps

    return render(request, 'camps/home.html', {'camps_by_category': camps_by_category})


def category_camps(request, category_name):
    category_dict = dict(Camp.CATEGORY_CHOICES)

    if category_name not in category_dict:
        raise Http404("Category not found")

    camps = Camp.objects.filter(category=category_name)
    return render(request, 'camps/category_camps.html', {
        'category_display': category_dict[category_name],
        'camps': camps
    })

def camp_detail(request, camp_id):
    camp = get_object_or_404(Camp, id=camp_id)
    return render(request, 'camps/camp_detail.html', {'camp': camp})