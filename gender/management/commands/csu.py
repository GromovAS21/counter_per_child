import os

import django
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):

        try:
            superuser = User.objects.create_superuser(
                username=os.getenv("ADMIN_USERNAME"),
            )
            superuser.set_password(os.getenv("ADMIN_PASSWORD"))
            superuser.save()

        except django.db.utils.IntegrityError:
            self.stdout.write(self.style.ERROR("SUPERUSER ALREADY CREATED"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
        else:
            self.stdout.write(self.style.SUCCESS("SUPERUSER CREATE SUCCESS"))
