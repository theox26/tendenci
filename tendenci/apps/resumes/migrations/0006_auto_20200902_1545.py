# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0005_auto_20190816_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='resume',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
    ]
