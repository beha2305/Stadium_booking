from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **kwargs):

        if not phone_number:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None):

        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        user.save()
        return user


class Permission(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=100)
    permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number