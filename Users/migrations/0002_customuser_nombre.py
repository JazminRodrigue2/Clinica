# Generated by Django 4.2 on 2024-06-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
