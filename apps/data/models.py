from django.db import models
from django.db.models import JSONField


class About(models.Model):
    name = models.CharField(max_length=32, verbose_name="Nomi o'zbek")
    text = models.TextField(max_length=1024, null=True, verbose_name="Matn o'zbek")

    name_ru = models.CharField(max_length=32, verbose_name="Nomi rus", null=True)
    text_ru = models.TextField(max_length=1024, null=True, verbose_name="Matn rus")

    image = models.ImageField(upload_to='images/', null=True, verbose_name="Rasm")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"


class Language(models.Model):
    oz = JSONField(default=dict, verbose_name="O'zbek")
    ru = JSONField(default=dict, verbose_name="Руский")

    def __str__(self):
        return "Bot so'zlari"

    class Meta:
        verbose_name = "So'z"
        verbose_name_plural = "So'zlar"


class Courses(models.Model):
    name = models.CharField(max_length=32, verbose_name="Nomi o'zbek")
    description = models.TextField(max_length=1024, null=True, verbose_name="Kurs haqida ma'lumot o'zbek")

    name_ru = models.CharField(max_length=32, null=True, verbose_name="Nomi rus")
    description_ru = models.TextField(max_length=1024, null=True, verbose_name="Kurs haqida ma'lumot rus")

    image = models.ImageField(upload_to='images/', null=True, verbose_name="Kurs uchun rasm")
    telegram_group = models.URLField(max_length=256, null=True, verbose_name="Telegram guruhi demo dars uchun")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class CoursesDescription(models.Model):
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description[:100]


class Faq(models.Model):
    faq = models.TextField(max_length=4096, verbose_name="Ko'p beriladigan savollar o'zbek")
    faq_ru = models.TextField(max_length=4096, null=True, verbose_name="Ko'p beriladigan savollar rus")

    def __str__(self):
        return self.faq[:100]

    class Meta:
        verbose_name = "Ko'p beriladigan savollar"
        verbose_name_plural = "Ko'p beriladigan savollar"


class ContactInfo(models.Model):
    contact = models.TextField(max_length=512, verbose_name="Aloqa ma'lumotlari o'zbek")
    contact_ru = models.TextField(max_length=512, verbose_name="Aloqa ma'lumotlari rus", null=True)

    def __str__(self):
        return self.contact[:100]

    class Meta:
        verbose_name = "Aloqa ma'lumotlari"
        verbose_name_plural = "Aloqa ma'lumotlari"


class StartText(models.Model):
    text = models.TextField(max_length=1024, verbose_name="Start matni o'zbek")
    text_ru = models.TextField(max_length=1024, null=True, verbose_name="Start matni rus")

    def __str__(self):
        return self.text[:100]

    class Meta:
        verbose_name = "Start matni"
        verbose_name_plural = "Start matni"
