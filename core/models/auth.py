from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class UserProfileManager(BaseUserManager):

    def _create_user(self, first_name, last_name, email, password, is_superuser, is_staff):
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email)
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.set_password(password)
        user.save()
        return user

    def create_user(self, first_name, last_name, email, password):
        return self._create_user(first_name, last_name, email, password, False, True)

    def create_superuser(self, first_name, last_name, email, password):
        return self._create_user(first_name, last_name, email, password, True, True)


class UserProfile(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
