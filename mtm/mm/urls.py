from django.urls import path
from .views import index, param

urlpatterns = [
    path('', index),
    path('worktype/<int:work_type_id>/', param, name='param'),
]