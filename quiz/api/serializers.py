from rest_framework import serializers
from  quiz.models import  Question, Answer, Quizzes
        
class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)
    
    class Meta:    
        model = Question
        fields = [
            'id',
            'title',
            'quiz',
            'question',
            'image',
            'answer',
        ]
