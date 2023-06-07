from django.urls import path
from .views import user_log_view

app_name = 'log'

urlpatterns = [
    path('', user_log_view, name='user_log'),
]