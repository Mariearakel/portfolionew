# Generated by Django 4.2.2 on 2023-07-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_alter_personaldata_who_i_am'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=20)),
                ('email', models.TextField(max_length=20)),
                ('phone', models.PositiveBigIntegerField()),
            ],
        ),
    ]
