from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, username, email, firstName, lastName, password=None):
        if not username:
            raise ValueError("Invalid username")
        if not email:
            raise ValueError("Invalid email")
        if not firstName:
            raise ValueError("Invalid first name")
        if not lastName:
            raise ValueError("Invalid last name")

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            firstName = firstName,
            lastName = lastName,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, firstName, lastName, password=None):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            firstName = firstName,
            lastName = lastName,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

# Create your models here.
class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email", max_length=50, unique=True, blank=True)
    username        = models.CharField(verbose_name="username", max_length=30, unique=True, blank=True)
    firstName       = models.CharField(max_length=50, blank=True)
    lastName        = models.CharField(max_length=30, blank=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','firstName','lastName']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True