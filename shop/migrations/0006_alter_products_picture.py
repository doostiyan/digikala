# Generated by Django 5.0.6 on 2024-07-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_products_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
