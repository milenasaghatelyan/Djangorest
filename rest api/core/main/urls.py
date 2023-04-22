from django.urls import path
from .views import *

urlpatterns = [
    path('CarViewsJson/' , CarAPIView.as_view())
]