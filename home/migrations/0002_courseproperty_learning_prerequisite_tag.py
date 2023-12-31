# Generated by Django 3.1.3 on 2023-03-29 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('courseproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.courseproperty')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='home.course')),
            ],
            bases=('home.courseproperty',),
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('courseproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.courseproperty')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prerequisites', to='home.course')),
            ],
            bases=('home.courseproperty',),
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('courseproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.courseproperty')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learnings', to='home.course')),
            ],
            bases=('home.courseproperty',),
        ),
    ]
