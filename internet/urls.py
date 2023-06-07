from django.urls import path
from . import views

app_name = 'internet'

urlpatterns = [
    path('', views.browser, name='browser'),
]
