# Generated by Django 3.1.3 on 2023-03-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnails')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resource', models.FileField(upload_to='files/resources')),
                ('length', models.IntegerField(default=0)),
            ],
        ),
    ]
