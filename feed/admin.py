from django.contrib import admin


# Register your models here.
from .models import PhysicalActivity,Category,Question,Answer,Place,Event, Article

admin.site.register(PhysicalActivity)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Article)
