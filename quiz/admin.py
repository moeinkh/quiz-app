from django.contrib import admin
from .models import Category, Question, Answer
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

# @admin.register(Answer)
class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

    inlines = [AnswerInline]