# Generated by Django 4.2.6 on 2024-01-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_asar_nomi_asarlar_comment_alter_asarlar_b_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bayt_parse',
            name='mano',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
