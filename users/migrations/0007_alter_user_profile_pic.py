# Generated by Django 4.2.7 on 2024-06-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='user_pic/logo.png', upload_to='user_pic'),
        ),
    ]
