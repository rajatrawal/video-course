# Generated by Django 3.1.3 on 2023-03-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230329_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproperty',
            name='discription',
            field=models.CharField(max_length=100),
        ),
    ]
