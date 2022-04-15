# Generated by Django 4.0.3 on 2022-04-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('pedido', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Otro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
                ('pedido', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Partes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('pedido', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vidriera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('pedido', models.BooleanField()),
            ],
        ),
    ]