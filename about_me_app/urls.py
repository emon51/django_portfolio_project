
from django.urls import path
from about_me_app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('education/', views.education, name = 'education'),
    path('contact/', views.contact, name = 'contact'),
]