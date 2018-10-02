from django.urls import path
from django.contrib import admin
from feed.views import UserCreateAPIView, FilteredPlaces,FilteredEvents, PhysicalActivitiesList, CategoryDetailView, QuestionDetail, AnswerDetail, PlaceList, EventList
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),



    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    
    path('physicalActivitiesList/', PhysicalActivitiesList.as_view(), name='api-plan-List'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),
    path('answer/<int:id>/', AnswerDetail.as_view(), name='answer-detail'),
    path('places/', PlaceList.as_view(), name='places'),
    path('event/', EventList.as_view(), name='event'),
    path('filterPlaces/<int:id>', FilteredPlaces.as_view(), name='filterPlaces'),
    path('filterEvents/<int:id>', FilteredEvents.as_view(), name='filterEvents'),

]

if settings.DEBUG:
   urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
