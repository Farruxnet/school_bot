# Generated by Django 4.1.3 on 2022-12-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_remove_contactinfo_faq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'Biz haqimizda', 'verbose_name_plural': 'Biz haqimizda'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': "Aloqa ma'lumotlari", 'verbose_name_plural': "Aloqa ma'lumotlari"},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Kurs', 'verbose_name_plural': 'Kurslar'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': "Ko'p beriladigan savollar", 'verbose_name_plural': "Ko'p beriladigan savollar"},
        ),
        migrations.AlterModelOptions(
            name='starttext',
            options={'verbose_name': 'Start matni', 'verbose_name_plural': 'Start matni'},
        ),
        migrations.AddField(
            model_name='courses',
            name='telegram_group',
            field=models.CharField(max_length=256, null=True, verbose_name='Telegram guruhi demo dars uchun'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(max_length=1024, null=True, verbose_name='Matn'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact',
            field=models.TextField(max_length=512, verbose_name="Aloqa ma'lumotlari"),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(max_length=1024, null=True, verbose_name="Kurs haqida ma'lumot"),
        ),
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Kurs uchun rasm'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Nomi'),
        ),
    ]