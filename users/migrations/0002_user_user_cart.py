# Generated by Django 4.2.7 on 2024-06-10 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='baseapp.cart'),
        ),
    ]
