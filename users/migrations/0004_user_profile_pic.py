# Generated by Django 4.2.7 on 2024-06-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_user_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='user_pic/avatat.png', upload_to='user_pic'),
        ),
    ]
