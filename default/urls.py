from django.urls import path
from .veiws import *

urlpatterns = [
    path('poll/', poll_list),
    path('poll1/', PollList.as_view()),
]