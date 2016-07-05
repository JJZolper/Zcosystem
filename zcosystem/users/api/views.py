from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from stream_django.enrich import Enrich

from users.models import *
from users.api.serializers import *

# User Profile List
class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# User Profile Retrieve Update Destroy
class UserProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# User Event List
class UserEventList(generics.ListAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

# User Event Create
class UserEventCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# User Event Retrieve Update Destroy
class UserEventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

# User Event City List
@permission_classes((permissions.AllowAny,))
class UserEventCityList(APIView):
    """
    Retrieve the user events for a given city.
    """
    def get(self, request, cityslug, format=None):
        '''
        enricher = Enrich()
        flat_feed = feed_manager.get_news_feed(cityslug)['flat']
        activities = feed.get(limit=25)['results']
        enriched_activities = enricher.enrich_activities(activities)
        '''
        '''
        UserEventsQuerySet = UserEvent.objects.filter(city__slug = cityslug).order_by('-created_at')[:3600]
        serialized = UserEventSerializer(UserEventsQuerySet, many=True)
        return Response(serialized.data)
        '''
        enricher = Enrich()
        feed = feed_manager.get_feed('cityevents', cityslug)
        activities = feed.get(limit=25)['results']
        enriched_activities = enricher.enrich_activities(activities)
        serialized = UserEventSerializer(enriched_activities, many=True)
        return Response(serialized.data)







'''
# User Event City List
class UserEventCityList(generics.ListAPIView):
    serializer_class = UserEventSerializer
    queryset = UserEvent.objects.order_by('-created_at').all()
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get(self, request, format=None):
        """
        Returns a JSON response with a listing of course objects
        """
        paginator = PageNumberPagination()
        # From the docs:
        # The paginate_queryset method is passed the initial queryset
        # and should return an iterable object that contains only the
        # data in the requested page.
        result_page = paginator.paginate_queryset(self.get_queryset(), request)
        # Now we just have to serialize the data.
        serializer = UserEventSerializer(result_page, many=True, context={'request': request})
        # From the docs:
        # The get_paginated_response method is passed the serialized page
        # data and should return a Response instance.
        return paginator.get_paginated_response(serializer.data)
'''





