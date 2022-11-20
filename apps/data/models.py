from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name

class CoursesDescription(models.Model):
    description = models.TextField(max_length = 1024)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.description[:100]

class Faq(models.Model):
    faq = models.TextField(max_length=4096)

    def __str__(self):
        return self.faq[:100]

class ContactInfo(models.Model):
    contact = models.TextField(max_length=512)

    faq = models.TextField(max_length=4096)

    def __str__(self):
        return self.contact[:100]
