from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Place, Tag, Review
from .serializers import PlaceModelSerializer, TagModelSerializer, ReviewModelSerializer

# Create your views here.


class PlaceView(ModelViewSet):
    serializer_class = PlaceModelSerializer
    queryset = Place.objects.all()


class TagView(ModelViewSet):
    serializer_class = TagModelSerializer
    queryset = Tag.objects.all()


class ReviewView(ModelViewSet):
    serializer_class = ReviewModelSerializer
    queryset = Review.objects.all()
