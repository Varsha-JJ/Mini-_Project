# Generated by Django 4.1.2 on 2022-11-20 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_filter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
