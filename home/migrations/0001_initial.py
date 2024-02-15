# Generated by Django 4.2.6 on 2024-01-20 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Asarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asar_nomi', models.CharField(max_length=100)),
                ('asar_all_text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='B_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('a_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.a_category')),
            ],
        ),
        migrations.CreateModel(
            name='Bayt_parse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('b_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.b_category')),
            ],
        ),
        migrations.CreateModel(
            name='N_kirib_kelgan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('til_turi_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nasriy_bayon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('b_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.b_category')),
                ('bayt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bayt_parse')),
            ],
        ),
        migrations.CreateModel(
            name='N_lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('izohlar', models.TextField()),
                ('kirib_kelgan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.n_kirib_kelgan')),
            ],
        ),
    ]
