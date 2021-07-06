from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Quizzes)
admin.site.register(models.Answer)

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInlineModel, 
        ] 


