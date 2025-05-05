from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('add/', views.add_camp, name='add_camp'),  # ใช้ 'add/' เป็นเส้นทางหลักสำหรับเพิ่มค่าย
    path('category/<str:category_slug>/', views.category_camps, name='category_camps'),
    path('camp/<int:camp_id>/', views.camp_detail, name='camp_detail'),
    path('profile/', views.profile, name='profile'),
]