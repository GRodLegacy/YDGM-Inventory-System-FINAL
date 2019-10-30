# Generated by Django 2.2.6 on 2019-10-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('item', models.CharField(max_length=25)),
                ('site', models.CharField(max_length=10)),
                ('purchased_price', models.IntegerField()),
                ('posted_date', models.CharField(max_length=15)),
                ('bought_at', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('item', models.CharField(max_length=25)),
                ('site', models.CharField(max_length=10)),
                ('purchased_price', models.IntegerField()),
                ('posted_date', models.CharField(max_length=15)),
                ('bought_at', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('item', models.CharField(max_length=25)),
                ('site', models.CharField(max_length=10)),
                ('purchased_price', models.IntegerField()),
                ('posted_date', models.CharField(max_length=15)),
                ('bought_at', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]