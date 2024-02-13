"""
URL configuration for gwSystems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views as my_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('faqs', my_views.faqs, name='faqs-url'),
    path('services', my_views.services, name='services-url'),
    path('portfolio', my_views.portfolio, name='portfolio-url'),
    path('techstack', my_views.techstack, name='techstack-url'),
    path('testimonials', my_views.testimonial, name='testimonials-url'),
    path('blog', my_views.blog, name='blog-url'),
    path('partner', my_views.partner, name='partner-url'),
    path('contact', my_views.contact, name='contact-url'),
]
