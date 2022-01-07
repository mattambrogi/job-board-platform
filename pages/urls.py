from django.urls import path
from .views import HomePageView, LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name = 'home') #changed from HomePageView
]
