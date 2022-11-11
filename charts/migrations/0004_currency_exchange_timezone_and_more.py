# Generated by Django 4.1.2 on 2022-11-11 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_chart_ticker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('symbol', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=25)),
                ('market_id', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('country_code', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('website', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(max_length=25)),
                ('abbr', models.CharField(max_length=10)),
                ('abbr_dst', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='ticker',
            old_name='currency_country',
            new_name='stock_exchange',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='currency_code',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='currency_name',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='currency_number',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='description',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='exchange',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='sector',
        ),
        migrations.AddField(
            model_name='ticker',
            name='has_eod',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticker',
            name='has_intraday',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticker',
            name='symbol',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='Intraday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=25)),
                ('market_id', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('country_code', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('datetime', models.DateTimeField()),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.ticker')),
            ],
        ),
    ]