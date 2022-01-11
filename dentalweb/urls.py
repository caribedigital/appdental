from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('pricing/', views.pricing, name="pricing"),
    path('blog/', views.blog, name="blog"),
    path('blog_details', views.blog_details, name="blog-details"),
    path('contact', views.contact, name="contact"),
]