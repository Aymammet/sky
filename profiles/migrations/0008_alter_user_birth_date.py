# Generated by Django 4.1.5 on 2023-04-28 02:34

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_user_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, validators=[profiles.models.validate_past_date]),
        ),
    ]
