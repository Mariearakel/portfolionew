# Generated by Django 4.2.2 on 2023-07-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0023_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=1000),
        ),
    ]
