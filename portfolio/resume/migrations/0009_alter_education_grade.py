# Generated by Django 4.2.2 on 2023-07-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_skill_name_alter_skill_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='grade',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
