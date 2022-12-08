from django.db import models

class Messages(models.Model):
    IS_ANSWER = (
        (True, "Javob berilgan"),
        (False, "Javob berilmagan"),
    )
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    message_id = models.BigIntegerField(default=0)
    message = models.TextField(verbose_name="Xabar matni")
    answer = models.TextField(null=True, verbose_name="Xabar uchun Javob")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")
    is_answer = models.BooleanField(choices=IS_ANSWER, default=False, verbose_name="Javob berildimi?")

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

class Settings(models.Model):
    admin = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sozlamalari"
        verbose_name_plural = "Sozlamalari"
class Register(models.Model):
    SEX = (
        ('man', "Erkak"),
        ('woman', "Ayol"),
    )
    STATUS = (
        (True, "To'liq ro'yxatdan o'tgan"),
        (False, "To'liq ro'yxatdan o'tgmagan"),
    )
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name='Foydalanuvchi')
    course = models.ForeignKey('data.Courses', on_delete=models.SET_NULL, null=True, verbose_name="Kurs")
    name = models.CharField(max_length=64, null=True, verbose_name="Ismi")
    sex = models.CharField(choices=SEX, max_length=10, null=True, verbose_name="Jinsi")
    address = models.TextField(max_length=255, null=True, verbose_name="Manzil")
    phone = models.CharField(max_length=20, null=True, verbose_name="Telefon")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")
    username = models.CharField(max_length=32, null=True)
    status = models.BooleanField(choices=STATUS, default=False, verbose_name="Holati")

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = "Kusrga yozilgan"
        verbose_name_plural = "Kusrga yozilganlar"
