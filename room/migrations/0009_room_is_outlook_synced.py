# Generated by Django 2.2.6 on 2020-06-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_room_is_google_synced'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_outlook_synced',
            field=models.BooleanField(default=False),
        ),
    ]