# Generated by Django 4.1.2 on 2022-11-11 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0005_ticker_currency_ticker_timezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticker',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='timezone',
        ),
        migrations.AddField(
            model_name='exchange',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charts.currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exchange',
            name='timezone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charts.timezone'),
            preserve_default=False,
        ),
    ]
