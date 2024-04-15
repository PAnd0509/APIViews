from django.urls import path
from .views import *

urlpatterns=[
    path('projects/',ProjectAPIView.as_view()),
    path('tasks/',TaskAPIView.as_view())
]


    


