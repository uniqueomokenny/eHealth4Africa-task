from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, full_name, password=None):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, full_name, password):
        user = self.create_user(email, username, full_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    username = models.CharField(max_length=120, unique=True, verbose_name="Username")
    full_name = models.CharField(max_length=120, verbose_name="Full name")
    created_at = models.DateTimeField(auto_now_add=True)
    is_medical_practioner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email", "full_name"]
    USERNAME_FIELD = "username"

    objects = UserManager()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split(" ")[0]

    def __str__(self):
        return str(self.username) if self.username else ''

    class Meta:
        ordering = ("-created_at",)

