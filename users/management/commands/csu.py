from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from factory.models import NetworkNode
from users.models import User


class Command(BaseCommand):
    help = 'Creates a superuser and fills the database with initial data.'

    def handle(self, *args, **options):
        # Создаем суперпользователя
        user = User.objects.create(
            email='admin@test.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('2368')
        user.save()

        # Заполняем базу данных начальными данными
        initial_data = [
            {
                'name': 'Factory 1',
                'email': 'factory1@example.com',
                'country': 'Country 1',
                'city': 'City 1',
                'street': 'Street 1',
                'house_number': '1',
                'debt': 0,
                'level': 0
            },
            {
                'name': 'Retail Network 1',
                'email': 'retail1@example.com',
                'country': 'Country 2',
                'city': 'City 2',
                'street': 'Street 2',
                'house_number': '2',
                'debt': 0,
                'level': 1
            },
            {
                'name': 'Individual Entrepreneur 1',
                'email': 'entrepreneur1@example.com',
                'country': 'Country 3',
                'city': 'City 3',
                'street': 'Street 3',
                'house_number': '3',
                'debt': 0,
                'level': 2
            }
        ]

        for data in initial_data:
            try:
                NetworkNode.objects.create(**data)
                self.stdout.write(self.style.SUCCESS(f'NetworkNode {data["name"]} created successfully.'))
            except IntegrityError:
                self.stdout.write(self.style.ERROR(f'NetworkNode {data["name"]} already exists.'))
