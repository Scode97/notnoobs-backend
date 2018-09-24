from django.conf import settings

from rest_framework import serializers
from .models import PhysicalActivities


class PhysicalActivitiySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalActivities
        fields = "__all__"
         
            