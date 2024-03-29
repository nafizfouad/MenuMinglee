# Generated by Django 4.1.1 on 2024-01-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
