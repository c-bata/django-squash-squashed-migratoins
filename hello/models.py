from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=20, default='')
    choice2 = models.CharField(max_length=20, default='')
