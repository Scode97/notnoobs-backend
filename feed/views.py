from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import PhysicalActivity, Category, Question, Answer, Place, Event
from .serializers import UserCreateSerializer, PhysicalActivitiySerializer, CategoryDetailSerializer, QuestionSerialzer, AnswerSerialzer, PlaceSerializer, EventSerializer

# Create your views here.
class PhysicalActivitiesList(ListAPIView):
	queryset = PhysicalActivity.objects.all()
	serializer_class = PhysicalActivitiySerializer

class CategoryDetailView(RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryDetailSerializer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'



class AnswerDetail(RetrieveAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerialzer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'


class QuestionDetail(RetrieveAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerialzer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'

class PlaceList(ListAPIView):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer


class EventList(ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer




class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class FilteredPlaces(ListAPIView):
	serializer_class = PlaceSerializer


	def get_queryset(self):
		id = self.kwargs['id']
		return Place.objects.filter(category__in=[id])
























