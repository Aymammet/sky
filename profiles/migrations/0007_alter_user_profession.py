# Generated by Django 4.1.5 on 2023-04-28 02:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_user_bio_alter_user_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MaxLengthValidator(25)]),
        ),
    ]
