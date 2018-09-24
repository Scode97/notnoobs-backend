from django.urls import path
from django.contrib import admin
from feed.views import PhysicalActivitiesList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('physicalActivitiesList/', PhysicalActivitiesList.as_view(), name='api-plan-List'),
]
