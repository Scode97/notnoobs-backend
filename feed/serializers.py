from django.conf import settings

from rest_framework import serializers
from .models import PhysicalActivity
from .models import Category, Answer, Question


class PhysicalActivitiySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalActivity
        fields = "__all__"


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class QuestionSerialzer(serializers.ModelSerializer):
	class Meta:
		model = Question 
		fields = "__all__"

class AnswerSerialzer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = "__all__"

         
            