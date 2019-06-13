from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker
import random
from questions.models import Profile, Tag, Question

fake = Faker()

class Command(BaseCommand):

	help = 'Create random questions'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='The number of questions to be created')

	def handle(self, *args, **kwargs):
		total = kwargs['total']

		for i in range(1,15):

			p = Profile.objects.get(pk=i)
			# все теги

			for k in range(0,3):

				for j in range(0,2):

					tag_1 = Tag.objects.get(pk=random.randint(1, 20))
					tag_2 = Tag.objects.get(pk=random.randint(1, 20))
					while tag_1 == tag_2:
						tag_2 = Tag.objects.get(pk=random.randint(1, 20))

				#Тут ошибка в tags.set
				question = Question(author=p, title=fake.sentence(), content=fake.text())
				#question.save()


			#Profile.objects.create_user(username=fake.name(), email=fake.email(), password='123')

		