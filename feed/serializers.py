from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PhysicalActivity
from .models import Category, Answer, Question, Place, Event, Booking, Article
from django.dispatch import receiver
from rest_framework_jwt.settings import api_settings




from django.db.models.signals import post_save


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

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"
         
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

# FOR Users

class UserCreateSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password','token', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        print (validated_data)
        username = validated_data['username']
        password = validated_data['password']
        firstname = validated_data['first_name']
        lastname = validated_data['last_name']
        email = validated_data['email']
     



        new_user = User(username=username, first_name= firstname, last_name= lastname, email=email)
        new_user.set_password(password)
          

        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        handler =jwt_payload_handler(new_user)

        
        token = jwt_encode_handler(handler)

        validated_data["token"] = token

        print (validated_data)

        return validated_data