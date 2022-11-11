# Generated by Django 4.1.2 on 2022-11-04 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summaryapp', '0002_alter_assingmentmodel_tip'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='assingmentmodel',
            name='service',
        ),
        migrations.AddField(
            model_name='assingmentmodel',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='summaryapp.servicemodel'),
            preserve_default=False,
        ),
    ]
