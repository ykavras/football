from django.urls import path

from .views import ApplyView

app_name = 'apply'

urlpatterns = [
    path('', ApplyView.as_view(), name='apply')
]
