# Generated by Django 4.1.2 on 2022-11-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image/'),
        ),
    ]
