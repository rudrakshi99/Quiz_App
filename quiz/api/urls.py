from django.urls import path
from .views import QuizListView, QuizQuestionView
app_name='quiz'

urlpatterns = [
     path('', QuizListView.as_view(), name='quiz'),
     path('q/<str:topic>/', QuizQuestionView.as_view(), name='questions' ),
]