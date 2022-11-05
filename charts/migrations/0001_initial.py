# Generated by Django 4.1.2 on 2022-11-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('symbol', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=150)),
                ('exchange', models.CharField(max_length=25)),
                ('currency_code', models.CharField(max_length=3)),
                ('currency_country', models.CharField(max_length=25)),
                ('currency_name', models.CharField(max_length=50)),
                ('currency_number', models.PositiveSmallIntegerField()),
                ('industry', models.CharField(max_length=25)),
                ('sector', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
