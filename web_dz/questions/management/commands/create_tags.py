from django.core.management.base import BaseCommand

from faker import Faker
from questions.models import Tag

fake = Faker()

class Command(BaseCommand):

	help = 'Create random  tags'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='The number of tags to be created')

	def handle(self, *args, **kwargs):
		total = kwargs['total']

		for i in range(total):

			t = Tag(title=fake.word())
			t.save()
