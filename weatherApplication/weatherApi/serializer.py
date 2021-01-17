from rest_framework import serializers

class SearchCity(serializers.Serializer):
    city_name=serializers.CharField(max_length=200)