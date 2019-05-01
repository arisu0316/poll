from django.urls import path
from .views import *

urlpatterns = [
    #path('poll/', poll_list),
    path('poll/', PollList.as_view()),
    path('poll/<int:pk>/', PollDetail.as_view()),
    path('vote/<int:oid>/', PollVote.as_view()),
    path('poll/create/', PollCreate.as_view()),
    path('poll/<int:pk>/update/',PollCreate.as_view()),
    path('poll/<int:pk>/delete/',PollDelete.as_view()),
    path('option/create/<int:pid>/',OptionCreate.as_view()),
    path('option/<int:pk>/update/',OptionCreate.as_view()),
    path('option/<int:pk>/delete/',OptionDelete.as_view()),
]