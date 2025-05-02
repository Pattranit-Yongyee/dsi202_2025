from django.urls import path
from .views import home, CampListView, CampDetailView

app_name = 'myapp'

urlpatterns = [
    # Home page at "/"
    path('', home, name='home'),
    # Camp list at "/camps/"
    path('camps/', CampListView.as_view(), name='camp-list'),
    # Camp detail at "/camps/<pk>/"
    path('camps/<int:pk>/', CampDetailView.as_view(), name='camp-detail'),
]
