from django.shortcuts import render, get_object_or_404
from .models import Question, Category

# Create your views here.
def home(request, id=None):
    category = Category.objects.all()

    return render(request, 'quiz/home.html', {
        'category': category,
    })    

def list_quiz(request, id): 
    question = Question.objects.all()

    if id:
        category = get_object_or_404(Category, id=id)
        question = question.filter(category=category)

    return render(request, 'quiz/quizes.html', {
        'question': question,
    })    
