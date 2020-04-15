# Generated by Django 2.2.6 on 2020-03-28 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('room_id', models.CharField(max_length=255)),
                ('room_type', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_rooms', to=settings.AUTH_USER_MODEL)),
                ('white_list', models.ManyToManyField(null=True, related_name='permissable_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
