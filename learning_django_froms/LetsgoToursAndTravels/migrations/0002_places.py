# Generated by Django 5.0.4 on 2024-07-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LetsgoToursAndTravels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
