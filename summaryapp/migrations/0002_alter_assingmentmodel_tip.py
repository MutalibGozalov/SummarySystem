# Generated by Django 4.1.2 on 2022-10-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assingmentmodel',
            name='tip',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
