# Generated by Django 3.0.4 on 2020-06-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200513_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='amount',
            field=models.IntegerField(blank=True, default=123),
            preserve_default=False,
        ),
    ]
