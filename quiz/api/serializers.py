from django.db import models
from rest_framework import serializers
from quiz.models import Category, Quizzes, QuizTakers, Question, Answer, UsersAnswer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        

class QuizListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    questions_count = serializers.SerializerMethodField()
    class Meta:
        model = Quizzes
        fields = ["id", "title", "date_created", "category", "questions_count"]
        read_only_fields = ["questions_count"]

    def get_questions_count(self, obj):
	    return obj.question_set.all().count()


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ["id", "question", "answer_text"]


class QuestionSerializer(serializers.ModelSerializer):
	answer_set = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = ("__all__")


class UsersAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsersAnswer
		fields = ("__all__")


class MyQuizListSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    questions_count = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Quizzes
        fields = ["id", "title", "category", "date_created", "questions_count", "completed", "score", "progress"]
        read_only_fields = ["questions_count", "completed", "progress"]

    def get_completed(self, obj):
        try:
            quiztaker = QuizTakers.objects.get(user=self.context['request'].user, quiz=obj)
            return quiztaker.completed
        except QuizTakers.DoesNotExist:
            return None

    def get_progress(self, obj):
        try:
            quiztaker = QuizTakers.objects.get(user=self.context['request'].user, quiz=obj)
            if quiztaker.completed == False:
                questions_answered = UsersAnswer.objects.filter(quiz_taker=quiztaker, answer__isnull=False).count()
                total_questions = obj.question_set.all().count()
                return int(questions_answered / total_questions)
            return None
        except QuizTakers.DoesNotExist:
            return None

    def get_questions_count(self, obj):
        return obj.question_set.all().count()

    def get_score(self, obj):
            try:
                quiztaker = QuizTakers.objects.get(user=self.context['request'].user, quiz=obj)
                if quiztaker.completed == True:
                    return quiztaker.score
                return None
            except QuizTakers.DoesNotExist:
                return None


class QuizTakerSerializer(serializers.ModelSerializer):
	usersanswer_set = UsersAnswerSerializer(many=True)

	class Meta:
		model = QuizTakers
		fields = ("__all__")


class QuizDetailSerializer(serializers.ModelSerializer):
	quiztaker_set = serializers.SerializerMethodField()
	question_set = QuestionSerializer(many=True)

	class Meta:
		model = Quizzes
		fields = ("__all__")

	def get_quiztaker_set(self, obj):
		try:
			quiz_taker = QuizTakers.objects.get(user=self.context['request'].user, quiz=obj)
			serializer = QuizTakerSerializer(quiz_taker)
			return serializer.data
		except QuizTakers.DoesNotExist:
			return None


class QuizResultSerializer(serializers.ModelSerializer):
	quiztaker_set = serializers.SerializerMethodField()
	question_set = QuestionSerializer(many=True)

	class Meta:
		model = Quizzes
		fields = ("__all__")

	def get_quiztaker_set(self, obj):
		try:
			quiztaker = QuizTakers.objects.get(user=self.context['request'].user, quiz=obj)
			serializer = QuizTakerSerializer(quiztaker)
			return serializer.data

		except QuizTakers.DoesNotExist:
			return None 
