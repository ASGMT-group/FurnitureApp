# Generated by Django 4.2.7 on 2024-06-10 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
