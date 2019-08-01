from django.db import models
from django.utils import timezone

import datetime


class Question(models.Model):

    class Meta:
        ordering = ['importance']
        verbose_name_plural = "questions"

    question_text = models.CharField(max_length=200, help_text='Include your question', unique=True)
    pub_date = models.DateTimeField('date published')
    importance = models.CharField(max_length=1, choices=(
        ('H','High'),('M','Medium'),('L','Low'),)) 

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

