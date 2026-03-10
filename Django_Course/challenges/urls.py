from . import views
from django.urls import path

# this urls for challenges application
urlpatterns = [
    path('january', views.index),   
]
