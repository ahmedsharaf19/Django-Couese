from . import views
from django.urls import path

# this urls for challenges application
urlpatterns = [
    #path('january', views.january),
    #path('february', views.febraury),
    #path('march', views.march),
    path('<month>', views.monthly_challenge)
]
