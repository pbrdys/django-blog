# Generated by Django 4.2.10 on 2024-03-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
