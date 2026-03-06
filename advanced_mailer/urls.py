from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email_view, name='advanced_send_email'),
    path('success/', views.success_view, name='advanced_success'),
    path('history/', views.history_view, name='advanced_history'),
    path('api/template/<int:pk>/', views.template_data_view, name='template_data'),
]
