from django.urls import path
from .views import *

urlpatterns = [
    #path('poll/', poll_list),
    path('poll/', PollList.as_view()),
    path('poll/<int:pk>/', PollDetail.as_view()),
    path('vote/<int:oid>/', PollVote.as_view()),
]