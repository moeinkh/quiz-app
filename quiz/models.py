from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    name = models.CharField(_('category name'), max_length=128)

    def __str__(self):
        return self.name

class Question(models.Model):   
    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')   

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category name'))
    title = models.CharField(_('title of the question'), max_length=128)

    created = models.DateTimeField(_('create time'), auto_now_add=True)
    updated = models.DateTimeField(_('update time'), auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('answers')

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_item', verbose_name=_('question name')) 
    answers = models.CharField(_('answer of the question'), max_length=128)  
    is_right = models.BooleanField(_('right?')) 

    created = models.DateTimeField(_('create time'), auto_now_add=True)
    updated = models.DateTimeField(_('update time'), auto_now=True)

    def __str__(self):
        return self.answers
