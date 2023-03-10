# Generated by Django 4.1.4 on 2023-01-02 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20221229_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
