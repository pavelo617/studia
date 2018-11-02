from django.urls import path, include
from .views import *

urlpatterns = [
    path('', info),
    path('work/', work),
    path('zarplata/', zarplata),
    path('anketa/', anketa),
    path('contact/', contact),
    path('phone/', phone),
]
