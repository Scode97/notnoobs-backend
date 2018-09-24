from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import PhysicalActivities
from .serializers import PhysicalActivitiySerializer

# Create your views here.
class PhysicalActivitiesList(ListAPIView):
	queryset = PhysicalActivities.objects.all()
	serializer_class = PhysicalActivitiySerializer