# Generated by Django 2.2.12 on 2022-12-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imageUrl',
            field=models.CharField(max_length=200),
        ),
    ]
