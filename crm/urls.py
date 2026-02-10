from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_lead, name='create_lead'),
    path('success/', views.lead_success, name='lead_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
