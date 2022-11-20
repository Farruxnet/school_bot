from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an phone_number')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    CHOICES = (
        ('oz', 'O\'zbek'),
        ('uz', 'Узбек'),
        ('ru', 'Руский'),
        ('en', 'Ingliz'),
    )
    tg_id = models.BigIntegerField(default=0, verbose_name = "Telegram ID")
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    language = models.CharField(choices=CHOICES, max_length=3)
    description = models.TextField(null=True, blank=True)

    STATUS_CHOICES = (
        ('0', "Botni o'chirgan"),
        ('1', "Faol"),
        ('2', "O'chirib qaytgan"),
    )

    status = models.CharField(default = '1', choices=STATUS_CHOICES, max_length=10)
    amount = models.IntegerField(default=0)
    step = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name="Foydalanuvchi"
        verbose_name_plural="Foydalanuvchilar"

    @property
    def is_staff(self):
        return self.is_admin






















########################
