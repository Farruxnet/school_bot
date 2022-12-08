# Generated by Django 4.1.3 on 2022-12-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_register_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Xabar', 'verbose_name_plural': 'Xabarlar'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Sozlamalari', 'verbose_name_plural': 'Sozlamalari'},
        ),
        migrations.AlterField(
            model_name='messages',
            name='answer',
            field=models.TextField(null=True, verbose_name='Xabar uchun Javob'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Vaqti'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='is_answer',
            field=models.BooleanField(choices=[(True, 'Javob berilgan'), (False, 'Javob berilmagan')], default=False, verbose_name='Javob berildimi?'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(verbose_name='Xabar matni'),
        ),
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.BooleanField(choices=[(False, "To'liq ro'yxatdan o'tgan"), (True, "To'liq ro'yxatdan o'tgmagan")], default=False, verbose_name='Holati'),
        ),
    ]
