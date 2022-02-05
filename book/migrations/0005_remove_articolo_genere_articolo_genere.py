# Generated by Django 4.0.2 on 2022-02-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_articolo_genere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articolo',
            name='genere',
        ),
        migrations.AddField(
            model_name='articolo',
            name='genere',
            field=models.ManyToManyField(to='book.Genere'),
        ),
    ]