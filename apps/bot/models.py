from django.db import models

class Messages(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    message_id = models.BigIntegerField(default=0)
    message = models.TextField()
    answer = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user}'

class Settings(models.Model):
    admin = models.ForeignKey('users.User', on_delete=models.CASCADE)
