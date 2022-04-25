from django.urls import path
from .views import home, list_quiz

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:id>/', list_quiz, name='list_quiz'),
]