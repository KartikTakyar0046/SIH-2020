# Generated by Django 3.0.2 on 2020-01-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
    ]
