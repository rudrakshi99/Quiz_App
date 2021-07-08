from django.contrib import admin
from .models import Quizzes, Question, Answer, UsersAnswer, QuizTaker, Category
import nested_admin

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4
    
class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline,]
    extra = 10
    
class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline,]
    
class UsersAnswerInline(admin.TabularInline):
    model = UsersAnswer
    
class QuizTakersAdmin(admin.ModelAdmin):
    inlines = [UsersAnswerInline,]
    
    
admin.site.register(QuizTaker, QuizTakersAdmin)
admin.site.register(Quizzes, QuizAdmin)
admin.site.register(UsersAnswer)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)

