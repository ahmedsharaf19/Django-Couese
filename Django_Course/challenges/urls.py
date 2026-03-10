from . import views
from django.urls import path

# this urls for challenges application
urlpatterns = [
    #path('january', views.january),
    #path('february', views.febraury),
    #path('march', views.march),
    
    # Order Is Differnce So must to be care
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name = 'month-challenge'),
    
]
