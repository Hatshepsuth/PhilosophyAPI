# Generated by Django 3.1.1 on 2020-09-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='author',
        ),
        migrations.AddField(
            model_name='philosopher',
            name='school',
            field=models.ManyToManyField(help_text='Select the schools of this thinker', related_name='philosophers', to='resources.School'),
        ),
    ]