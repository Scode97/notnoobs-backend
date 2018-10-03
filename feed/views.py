from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import PhysicalActivity, Category, Question, Answer, Place, Event, Booking, Article
from .serializers import UserCreateSerializer, PhysicalActivitiySerializer, CategoryDetailSerializer, QuestionSerialzer, AnswerSerialzer, PlaceSerializer, EventSerializer, BookingSerializer, ArticleSerializer

from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PhysicalActivitiesList(ListAPIView):
	queryset = PhysicalActivity.objects.all()
	serializer_class = PhysicalActivitiySerializer



#_____________Categories____________________________________

class CategoryDetailView(RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryDetailSerializer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'

#_____________Question and Answer____________________________

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


#___________________Places___________________________________

class PlaceList(ListAPIView):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer



class FilteredPlaces(ListAPIView):
	serializer_class = PlaceSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Place.objects.filter(category__in=[id])

class GetPlace(RetrieveAPIView):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'


#___________________Events___________________________________

class EventList(ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class FilteredEvents(ListAPIView):
	serializer_class = EventSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Event.objects.filter(category__in=[id])


class GetEvent(RetrieveAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'

#___________________Articles_________________________________

class ArticleList(ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class FilteredArticles(ListAPIView):
	serializer_class = ArticleSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Article.objects.filter(category__in=[id])

class GetArticle(RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'id'
	lookup_url_kwargs = 'id'


#___________________User_________________________________

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer



#________________Booking__________________________________

class CreateBooking(CreateAPIView):
	serializer_class = BookingSerializer
	# permission_classes = [IsAuthenticated]
	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)
       
class GetBooking(ListAPIView):
	serializer_class = BookingSerializer

	def get_queryset(self):
		return Booking.objects.filter(user=this.request.user)
	

























