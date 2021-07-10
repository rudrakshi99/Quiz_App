from django.conf import settings
from django.db import models
from accounts.models import User

def upload_location(instance, filename):
    return '/'.join(['Questionimages', str(instance.title), filename])


class Category(models.Model):
    class Meta:
        verbose_name_plural = ("Categories")

    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Quizzes(models.Model):

    class Meta:
        verbose_name = ("Quiz")
        verbose_name_plural = ("Quizzes")
        ordering = ['date_created']

    title = models.CharField(max_length=255, default=(
        "New Quiz"), verbose_name=("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    roll_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")
        ordering = ['date_created']
        
    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)    
    title = models.CharField(max_length=255, verbose_name=("Title"))
    question = models.TextField(null=False, default='')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    
    def __str__(self):
        return self.title


class Answer(models.Model):

    class Meta:
        verbose_name = ("Answer")
        verbose_name_plural = ("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(
        max_length=255, verbose_name=("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    
    

class QuizTaker(models.Model):
    
    class Meta:
        verbose_name = ("QuizTakers")
        verbose_name_plural = ("QuizTakers")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    date_finished = models.DateTimeField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class UsersAnswer(models.Model):
    
    class Meta:
        verbose_name = ("UsersAnswer")
        verbose_name_plural = ("UsersAnswers")

    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question.title
