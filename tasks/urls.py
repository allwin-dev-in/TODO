from django.urls import path

from tasks.views import SignupView
from tasks.views import TaskCreateListView
from tasks.views import TaskRetriveUpdateDeleteView

urlpatterns=[
    path("signup/",SignupView.as_view()),
    path("task/",TaskCreateListView.as_view()),
    path("task/<int:pk>/",TaskRetriveUpdateDeleteView.as_view()),
        
]