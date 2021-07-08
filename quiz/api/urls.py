from django.urls import path
from .views import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI
app_name='quiz'

urlpatterns = [
     path("my-quizzes/", MyQuizListAPI.as_view()),
	path("quizzes/", QuizListAPI.as_view()),
	path("save-answer/", SaveUsersAnswer.as_view()),
]