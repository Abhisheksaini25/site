from django.contrib import admin
from django.urls import path
from fun import views

admin.site.site_header = "Avi Admin"
admin.site.site_title = "Avi Admin Portal"
admin.site.index_title = "Welcome to Avi Admin Portal"

urlpatterns = [
    path("", views.home, name='home')
]