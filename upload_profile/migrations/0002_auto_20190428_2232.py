# Generated by Django 2.2 on 2019-04-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='introduce',
            field=models.TextField(),
        ),
    ]
