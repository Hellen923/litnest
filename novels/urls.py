# novels/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novel/<int:novel_id>/', views.novel_detail, name='novel_detail'),
    path('novel/<int:novel_id>/bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
]
