from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker
from questions.models import Profile

fake = Faker()

class Command(BaseCommand):

	help = 'Create random users'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='The number of users to be created')

	def handle(self, *args, **kwargs):
		total = kwargs['total']

		for i in range(total):

			u = User(username=fake.name(), email=fake.email(), password='123')
			u.save()
			p = Profile(user=u)
			p.save()
