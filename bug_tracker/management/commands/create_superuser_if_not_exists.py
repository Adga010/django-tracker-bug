import os
import getpass
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options):
        username = input('Enter superuser username: ')
        email = input('Enter email address: ')
        password = getpass.getpass('Enter password: ')

        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} already exists.'))
        except User.DoesNotExist:
            user = User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully.'))
