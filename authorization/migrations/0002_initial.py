# Generated by Django 4.0.4 on 2022-05-18 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('serials', '0001_initial'),
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='liked_serials',
            field=models.ManyToManyField(blank=True, to='serials.serial', verbose_name='Понравившиеся сериалы'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
