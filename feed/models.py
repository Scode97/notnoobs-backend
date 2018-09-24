from django.db import models

# Create your models here.
class PhysicalActivities(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField( default="")
    category = models.CharField(max_length=200)
    # category can be whether youtube video or place or event or etc
    link = models.URLField(max_length=500)

    def __str__(self):
    	return self.name