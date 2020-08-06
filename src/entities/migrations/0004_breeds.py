# Generated by Django 3.0.8 on 2020-08-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_auto_20200804_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alternative_name', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('lifespan', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'breeds',
            },
        ),
    ]
