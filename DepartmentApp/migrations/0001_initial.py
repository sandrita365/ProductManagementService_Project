# Generated by Django 4.1.13 on 2024-05-23 16:59

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
