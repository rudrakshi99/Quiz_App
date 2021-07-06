from django.db import models


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
        ordering = ['id']

    title = models.CharField(max_length=255, default=(
        "New Quiz"), verbose_name=("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")
        ordering = ['id']
        
    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)    
    title = models.CharField(max_length=255, verbose_name=("Title"))
    question = models.TextField(null=False, default='')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    is_active = models.BooleanField(
        default=False, verbose_name=("Active Status"))

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
