from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_slug>/', views.category_camps, name='category_camps'),
    path('camp/<int:camp_id>/', views.camp_detail, name='camp_detail'),  # เพิ่มเส้นทางนี้
]
