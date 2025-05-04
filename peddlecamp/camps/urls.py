from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_camp/', views.add_camp, name='add_camp'),  # เพิ่มเส้นทางนี้
    path('category/<str:category_slug>/', views.category_camps, name='category_camps'),
    path('camp/<int:camp_id>/', views.camp_detail, name='camp_detail'),
]