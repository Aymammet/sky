# Generated by Django 4.1.7 on 2023-06-07 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_message_receiver_alter_message_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='message.room'),
        ),
    ]
