# Generated by Django 4.2 on 2023-04-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_module', '0011_category_slug_alter_content_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='content',
            name='date',
            field=models.DateField(verbose_name='تاریخ انتشار'),
        ),
    ]