# Generated by Django 4.1.3 on 2022-12-10 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_alter_courses_telegram_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oz', models.TextField(verbose_name="O'zbek (max 1024)")),
                ('ru', models.TextField(null=True, verbose_name='Руский (max 1024)')),
                ('image', models.ImageField(upload_to='messages/', verbose_name='Rasm')),
                ('image_id', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Tele photo id')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Qo'shilgan vaqti")),
                ('count', models.IntegerField(default=0, verbose_name='Yuborilganlar soni')),
                ('not_send_count', models.IntegerField(default=0, verbose_name='Yuborilmaganlar soni')),
                ('status', models.BooleanField(default=False, verbose_name='Holati')),
            ],
            options={
                'verbose_name': 'Xabar yuborish',
                'verbose_name_plural': 'Xabarlar yuborish',
            },
        ),
    ]
