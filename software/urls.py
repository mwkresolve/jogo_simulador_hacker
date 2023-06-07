from django.urls import path
from .views import user_software_view

urlpatterns = [
    path('', user_software_view, name='user_software'),
]
