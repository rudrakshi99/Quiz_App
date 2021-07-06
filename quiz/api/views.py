from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from quiz.models import Question, Quizzes
from .serializers import  QuestionSerializer, QuizSerializer
from rest_framework import status

class QuizListView(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class QuizQuestionView(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


# class QuestionListCreateView(generics.ListCreateAPIView):

#     serializer_class = QuestionSerializer
#     queryset = Question.objects.all()

    
    