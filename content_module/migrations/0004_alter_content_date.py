# Generated by Django 4.2 on 2023-04-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_module', '0003_alter_content_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
