# Generated by Django 2.2.4 on 2020-01-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morae', '0003_auto_20200108_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='gphoto',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='family',
            name='tphoto',
            field=models.ImageField(upload_to=''),
        ),
    ]