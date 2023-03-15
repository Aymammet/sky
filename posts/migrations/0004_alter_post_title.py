# Generated by Django 4.1.5 on 2023-03-13 03:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_total_dislikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]