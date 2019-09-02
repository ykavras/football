from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('apply', apply, name='apply'),
    path('about', about, name='about'),
    path('sss', sss, name='sss'),
    path('privacy', privacy, name='privacy'),
    path('contact', contact, name='contact'),
]
