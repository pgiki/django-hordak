# Generated by Django 4.2.5 on 2024-03-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0037_auto_20230516_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='code'),
        ),
    ]
