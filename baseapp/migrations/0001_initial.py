# Generated by Django 4.2.7 on 2024-06-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='furniture_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField()),
                ('item_type', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('item_picture', models.ImageField(default='item_picturs/product.png', upload_to='item_picturs')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='baseapp.furniture_item')),
            ],
        ),
    ]