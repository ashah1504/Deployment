# Generated by Django 4.1.1 on 2022-09-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
