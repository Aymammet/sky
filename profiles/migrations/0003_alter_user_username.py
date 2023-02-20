# Generated by Django 4.1.5 on 2023-02-20 01:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
