# Generated by Django 4.2 on 2023-04-13 10:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_module', '0012_remove_category_slug_alter_content_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='date',
        ),
        migrations.AddField(
            model_name='content',
            name='rating',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
