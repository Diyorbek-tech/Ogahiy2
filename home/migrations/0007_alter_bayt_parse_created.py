# Generated by Django 4.2.6 on 2024-01-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bayt_parse_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bayt_parse',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
