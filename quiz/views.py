from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Category, Answer
from .form import AnswerForm
from django.contrib import messages
from django.urls import reverse

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
        question = question.filter(category=category).order_by('?')[:1]

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['is_right']:
                print(form.cleaned_data['is_right'])
                messages.success(request, 'جواب درست است.')
                return redirect(reverse('list_quiz', args=[id]))
            else:
                print(form.cleaned_data)
                messages.warning(request, 'جواب نادرست می باشد.')  
    else:
        form = AnswerForm()              

    return render(request, 'quiz/quizes.html', {
        'question': question,
    })    
