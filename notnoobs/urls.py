from django.urls import path
from django.contrib import admin
from feed.views import PhysicalActivitiesList, CategoryDetailView, QuestionDetail, AnswerDetail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('physicalActivitiesList/', PhysicalActivitiesList.as_view(), name='api-plan-List'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),
    path('answer/<int:id>/', AnswerDetail.as_view(), name='answer-detail')
]

if settings.DEBUG:
   urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
