# Generated by Django 2.2 on 2019-04-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_profile', '0003_auto_20190501_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]