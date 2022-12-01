from django.db import models

class Messages(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    message_id = models.BigIntegerField(default=0)
    message = models.TextField()
    answer = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'

class Settings(models.Model):
    admin = models.ForeignKey('users.User', on_delete=models.CASCADE)

class Register(models.Model):
    SEX = (
        ('man', "Erkak"),
        ('woman', "Ayol"),
    )
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name='Foydalanuvchi')
    course = models.ForeignKey('data.Courses', on_delete=models.SET_NULL, null=True, verbose_name="Kurs")
    name = models.CharField(max_length=64, null=True, verbose_name="Ismi")
    sex = models.CharField(choices=SEX, max_length=10, null=True, verbose_name="Jinsi")
    address = models.TextField(max_length=255, null=True, verbose_name="Manzil")
    phone = models.CharField(max_length=20, null=True, verbose_name="Telefon")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")
    username = models.CharField(max_length=32, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = "Kusrga yozilgan"
        verbose_name_plural = "Kusrga yozilganlar"
