from django.db import models

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

	def __str__ (self):
		return self.answer


class Question(models.Model):
	question = models.CharField(max_length=250)
	answers = models.ManyToManyField(Answer)

	def __str__ (self):
		return self.question
