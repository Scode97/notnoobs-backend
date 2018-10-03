from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhysicalActivity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField( default="")
    category = models.CharField(max_length=200)
    # category can be whether youtube video or place or event or etc
    link = models.URLField(max_length=500)

    def __str__(self):
    	return self.name


class Category(models.Model):
	name = models.CharField(max_length=200)
	subCategory = models.ManyToManyField('Category', blank=True)

	def __str__(self):
		return self.name


class Answer(models.Model):
	answer = models.CharField(max_length=100)
	quest = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,)

	def __str__ (self):
		return self.answer


class Question(models.Model):
	question = models.CharField(max_length=250)
	answers = models.ManyToManyField(Answer)

	def __str__ (self):
		return self.question

class Place(models.Model):
	name = models.CharField(max_length=250)
	category = models.ManyToManyField(Category)
	description = models.TextField()
	location = models.CharField(max_length=250)
	image = models.ImageField(blank=True)

	def __str__ (self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=250)
	category = models.ManyToManyField(Category)
	description = models.TextField()
	location = models.CharField(max_length=250)
	image = models.ImageField(blank=True)
	date_time = models.DateTimeField()
	price = models.DecimalField(max_digits=5, decimal_places=3)
	status = models.ForeignKey('Status', on_delete=models.CASCADE, blank=True)
	
	def __str__ (self):
		return self.name

class Status(models.Model):
	title = models.CharField(max_length=120)

	def __str__(self):
		return self.title

class Booking(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	seat = models.IntegerField()

	def __str__(self):
		return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField()
    category = models.ManyToManyField(Category)


    def __str__(self):
        return self.title


   


