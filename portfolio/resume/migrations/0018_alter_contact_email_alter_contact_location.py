# Generated by Django 4.2.2 on 2023-07-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.TextField(max_length=50),
        ),
    ]