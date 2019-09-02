from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('about', about, name='about'),
    path('sss', sss, name='sss'),
    path('privacy', privacy, name='privacy'),
    path('contact', contact, name='contact'),
]
