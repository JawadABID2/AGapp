# Generated by Django 4.2 on 2023-06-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAGRI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Time_Stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
