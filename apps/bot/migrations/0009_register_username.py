# Generated by Django 4.1.3 on 2022-12-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_register_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
    ]