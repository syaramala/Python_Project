# Generated by Django 5.1.4 on 2024-12-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
