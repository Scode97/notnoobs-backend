from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import PhysicalActivity, Category, Question, Answer, Place, Event, Booking
from .serializers import UserCreateSerializer, PhysicalActivitiySerializer, CategoryDetailSerializer, QuestionSerialzer, AnswerSerialzer, PlaceSerializer, EventSerializer, BookingSerializer

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

class GetEvent(RetrieveAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class FilteredPlaces(ListAPIView):
	serializer_class = PlaceSerializer


	def get_queryset(self):
		id = self.kwargs['id']
		return Place.objects.filter(category__in=[id])

class CreateBooking(CreateAPIView):
	serializer_class = BookingSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
       


class GetBooking(ListAPIView):
	serializer_class = BookingSerializer

	def get_queryset(self):
		return Booking.objects.filter(user=this.request.user)
	

class FilteredEvents(ListAPIView):
	serializer_class = EventSerializer


	def get_queryset(self):
		id = self.kwargs['id']
		return Event.objects.filter(category__in=[id])

























