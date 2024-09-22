from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Avi Admin"
admin.site.site_title = "Avi Admin Portal"
admin.site.index_title = "Welcome to Avi Admin Portal"

urlpatterns = [
    path("", views.index, name='home'),
    path("first/home", views.index, name='home'),
    path("first/about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]
