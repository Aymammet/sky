# Generated by Django 4.1.7 on 2023-06-07 03:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1500)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]