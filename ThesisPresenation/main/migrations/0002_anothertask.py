# Generated by Django 4.2.8 on 2023-12-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('limit', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]