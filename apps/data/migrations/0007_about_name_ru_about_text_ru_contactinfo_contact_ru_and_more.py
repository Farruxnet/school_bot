# Generated by Django 4.1.3 on 2022-12-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_about_options_alter_contactinfo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name_ru',
            field=models.CharField(max_length=32, null=True, verbose_name='Nomi rus'),
        ),
        migrations.AddField(
            model_name='about',
            name='text_ru',
            field=models.TextField(max_length=1024, null=True, verbose_name='Matn rus'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='contact_ru',
            field=models.TextField(max_length=512, null=True, verbose_name="Aloqa ma'lumotlari"),
        ),
        migrations.AddField(
            model_name='courses',
            name='description_ru',
            field=models.TextField(max_length=1024, null=True, verbose_name="Kurs haqida ma'lumot"),
        ),
        migrations.AddField(
            model_name='courses',
            name='name_ru',
            field=models.CharField(max_length=32, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='faq',
            name='faq_ru',
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AddField(
            model_name='starttext',
            name='text_ru',
            field=models.TextField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=32, verbose_name="Nomi o'zbek"),
        ),
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(max_length=1024, null=True, verbose_name="Matn o'zbek"),
        ),
    ]