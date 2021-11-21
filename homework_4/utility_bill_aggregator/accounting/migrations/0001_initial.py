# Generated by Django 3.2.9 on 2021-11-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64, verbose_name='Тип')),
                ('organization', models.CharField(max_length=64, verbose_name='Организация')),
                ('address', models.TextField(null=True, verbose_name='Адрес организации')),
            ],
        ),
    ]
