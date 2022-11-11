# Generated by Django 4.1.2 on 2022-11-11 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_currency_exchange_timezone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charts.currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticker',
            name='timezone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charts.timezone'),
            preserve_default=False,
        ),
    ]