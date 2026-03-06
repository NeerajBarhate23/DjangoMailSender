from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email_view, name='send_email'),
    path('success/', views.success_view, name='success'),
]
