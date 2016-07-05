from rest_framework import serializers

from django.contrib.auth.models import User

from users.models import *

# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ('name', 'short', 'slug')

# City Serializer
class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('name', 'slug', 'country')

# User Profile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('user', 'slug')

# User Event Serializer
class UserEventSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    
    class Meta:
        model = UserEvent
        fields = ('user', 'created_at', 'headline', 'city')



