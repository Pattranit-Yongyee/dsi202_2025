from django.urls import path
from .views import homepage, category_page, organize_camp, profile_page, search_camp

urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<int:category_id>/', category_page, name='category_page'),
    path('organize/', organize_camp, name='organize_camp'),
    path('profile/', profile_page, name='profile_page'),
    path('search/', search_camp, name='search_camp'),
]