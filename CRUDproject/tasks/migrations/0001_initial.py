# Generated by Django 3.2.7 on 2021-09-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True, verbose_name='Shape type')),
                ('status', models.CharField(choices=[('u', 'Area'), ('o', 'Perimeter')], max_length=1, verbose_name='Calculate shape')),
            ],
        ),
    ]
