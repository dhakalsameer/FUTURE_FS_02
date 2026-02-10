from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_lead, name='create_lead'),
    path('success/', views.lead_success, name='lead_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update-status/<int:lead_id>/', views.update_lead_status, name='update_lead_status'),

]
