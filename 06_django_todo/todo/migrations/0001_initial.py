# Generated by Django 4.2.3 on 2023-07-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('descrpition', models.TextField(blank=True)),
                ('priority', models.SmallIntegerField(choices=[(1, 'HIGH'), (2, 'MEDIUM'), (3, 'LOW')], default=3)),
                ('is_done', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
