# Generated by Django 5.0.7 on 2024-07-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('genres', models.ManyToManyField(to='app.genre')),
            ],
        ),
    ]
