# Generated by Django 4.2 on 2023-04-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_module', '0008_category_alter_content_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='long_description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='content',
            name='picture',
            field=models.ImageField(default=None, upload_to='content_module/upload', verbose_name='تصویر'),
        ),
    ]
