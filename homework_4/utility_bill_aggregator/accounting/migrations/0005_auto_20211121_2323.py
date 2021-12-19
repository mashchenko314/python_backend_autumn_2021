# Generated by Django 3.2.9 on 2021-11-21 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20211121_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['-year'], 'verbose_name': 'Счет', 'verbose_name_plural': 'Счета'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-type'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='mounth',
            new_name='month',
        ),
        migrations.AlterField(
            model_name='account',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.service', verbose_name='Тип услуги'),
        ),
    ]
