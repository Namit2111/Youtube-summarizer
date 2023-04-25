from .views import home
from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path('', home, name='home'),
    
]
