# Generated by Django 4.2.7 on 2024-06-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='user_pic/avatat.jpg', upload_to='user_pic'),
        ),
    ]
