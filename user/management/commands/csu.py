import os

import django
from django.core.management import BaseCommand

from gender.models import GenderChoices, Gender
from user.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        try:
            superuser = User.objects.create(
                email=os.getenv("ADMIN_USERNAME"),
                is_superuser=True,
                is_staff=True,
                is_active=True,
                first_name=os.getenv("ADMIN_FIRST_NAME"),
                second_name=os.getenv("ADMIN_SECOND_NAME"),
                last_name=os.getenv("ADMIN_LAST_NAME"),
            )
            superuser.set_password(os.getenv("ADMIN_PASSWORD"))
            superuser.save()
            Gender.objects.create(gender=GenderChoices.boy, user_id=superuser, image="children/admin_boy.png")
            Gender.objects.create(gender=GenderChoices.girl, user_id=superuser, image="children/admin_girl.png")

        except django.db.utils.IntegrityError:
            self.stdout.write(self.style.ERROR("SUPERUSER ALREADY CREATED"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
        else:
            self.stdout.write(self.style.SUCCESS("SUPERUSER CREATE SUCCESS"))
