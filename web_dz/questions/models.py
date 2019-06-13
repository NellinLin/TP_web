from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from questions.managers import QuestionManager

from .managers import *


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    #rating = models.IntegerField(default=0)
    avatar = models.ImageField(default="static/image/avatar.png")

    USERNAME_FIELD ='username'
    #TODO

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    title = models.CharField(max_length=64, verbose_name=u"Название тега")
    rating = models.IntegerField(default=0, verbose_name=u"Рейтинг тега")

    #objects = QuestionManager()
    objects = TagManager()

    def __str__(self):
        return self.title

class Question(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=0)
    title = models.CharField(default=0, max_length=128, verbose_name=u"Заголовок вопроса")
    text = models.TextField(default=0, verbose_name=u"Текст вопроса")

    rating = models.IntegerField(default=0, verbose_name=u"Рейтинг вопроса")

    tags = models.ManyToManyField(Tag, related_name='questions')
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")

    objects = QuestionManager()

    def __str__(self):
        return self.title




class Answer(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u"Текст ответа")

    rating = models.IntegerField(default=0, verbose_name=u"Рейтинг ответа")

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания ответа")

    objects = AnswerManager()
