# Generated by Django 4.0.4 on 2022-05-18 09:55

import authorization.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=authorization.models.user_directory_path, verbose_name='Фото')),
            ],
        ),
    ]
