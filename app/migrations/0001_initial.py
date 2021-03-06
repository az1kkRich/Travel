# Generated by Django 4.0.4 on 2022-05-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MazzaQilingYayrang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('malumoti', models.TextField()),
                ('narxi', models.IntegerField()),
                ('taklif', models.BooleanField()),
                ('image', models.ImageField(upload_to='MazzaQilibYayra')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Malumot',
                'verbose_name_plural': 'Malumot',
            },
        ),
    ]
