from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_camp, name='add_camp'),
    path('category/<str:category_slug>/', views.category_camps, name='category_camps'),
    path('camp/<int:camp_id>/', views.camp_detail, name='camp_detail'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
]