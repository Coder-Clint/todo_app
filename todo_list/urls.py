from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('reschedule/<list_id>', views.reschedule, name='reschedule'),
    path('scheduled/<list_id>', views.scheduled, name='scheduled'),
    path('edit/<list_id>', views.edit, name='edit'),

]
