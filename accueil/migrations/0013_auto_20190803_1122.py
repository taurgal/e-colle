# Generated by Django 2.2.3 on 2019-08-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0012_auto_20190803_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='semaine',
        ),
        migrations.AddField(
            model_name='programme',
            name='semaine',
            field=models.ManyToManyField(to='accueil.Semaine'),
        ),
    ]
