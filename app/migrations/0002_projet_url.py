# Generated by Django 4.1.7 on 2023-02-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='url',
            field=models.CharField(default='www.google.dz', max_length=50),
            preserve_default=False,
        ),
    ]
