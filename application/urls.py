from django.contrib import admin
from django.urls import path
from . import views

app_name = 'application'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('hw2/', views.hw2_page),
    path('hw5/', views.hw5_page),
    path('final/', views.final_page)
]
