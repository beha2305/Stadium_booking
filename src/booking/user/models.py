from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **kwargs):

        if not username:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            phone_number=phone_number,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):

        user = self.create_user(
            username,
            '',
            password=password,

        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    username = models.CharField(max_length=30, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Permission(models.Model):
    role = models.ManyToManyField(Role, related_name='roles')
    name = models.CharField(max_length=30)
    codename = models.CharField(max_length=200)

    def __str__(self):
        return self.name