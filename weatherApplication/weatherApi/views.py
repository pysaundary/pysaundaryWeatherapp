from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .getWeatherApi import get_weather
from rest_framework.status import HTTP_404_NOT_FOUND
from .serializer import SearchCity
from rest_framework.generics import mixins
from rest_framework import generics

# Create your views here.
class GetWeather(APIView):
    city_name=''
    api_key = "ab97b407c69ae7346f544843100d085b"

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        if len(self.city_name)<=0:
            self.city_name="london"
        data=get_weather(self.api_key,self.city_name)
        print(data)
        print("_____"*70)
        return Response(data)

    def post(self,request):
        """ 
        Post city Name 
        """
        self.city_name=request.data['city_name']
        data=get_weather(self.api_key,self.city_name)
        print(data)
        print("...."*20)
        return Response(data)