# Generated by Django 2.2.4 on 2019-10-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20191016_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='informes',
            name='diez',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='informes',
            name='sesenta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='informes',
            name='treinta',
            field=models.IntegerField(default=0),
        ),
    ]
