from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Content

# 1) FBV: Home page
def home(request):
    # no data needed here – just render a welcome page
    return render(request, 'myapp/home.html')

# 2) CBV: Camp list with search and status filter
class CampListView(ListView):
    model = Content
    template_name = 'myapp/camp_list.html'
    context_object_name = 'camps'
    paginate_by = 9  # optional: show 9 per page

    def get_queryset(self):
        qs = super().get_queryset()
        
        # คำค้นหาจากฟอร์ม
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(type__icontains=q) |
                Q(description__icontains=q) |
                Q(detail__icontains=q)
            )

        # กรองค่ายตามสถานะ "เปิดรับสมัคร" หรือ "ปิดรับสมัคร"
        is_open = self.request.GET.get('is_open', '').strip()
        if is_open == 'true':
            qs = qs.filter(is_open=True)
        elif is_open == 'false':
            qs = qs.filter(is_open=False)

        return qs

# 3) CBV: Camp detail
class CampDetailView(DetailView):
    model = Content
    template_name = 'myapp/camp_detail.html'
    context_object_name = 'camp'
