# Generated by Django 5.0.4 on 2024-04-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]