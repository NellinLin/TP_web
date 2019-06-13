from django.db import models
from .models import *


class QuestionManager(models.Manager):
    def get_by_tag(self, _tag):
        return self.all().filter(title=_tag)

    def get_by_id(self, question_id):
        return self.get(id = question_id)

    def sort_by_question_date(self):
        return self.all().order_by('create_date').reverse()

    def sort_by_question_rating(self):
        return self.all().order_by('rating').reverse()

    def sort_by_id(self, qid):
        return self.all().filter(id=qid)

class TagManager(models.Manager):
    def get_all_tags(self):
        return self.all()


class AnswerManager(models.Manager):
    def sort_by_answer_rating(self):
        return self.all().order_by('rating').reverse()

    def get_answer_by_question(self, question_id):
        return self.all().filter(question = question_id)