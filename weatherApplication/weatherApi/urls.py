from django.urls import path
from .views import *
app_name="weatherApi"

urlpatterns = [
    path('main_page/',GetWeather.as_view(),name='get_weather'),
]
