# Generated by Django 4.0.5 on 2023-02-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Date', models.DateField()),
                ('Description', models.TextField(max_length=40000)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Venue', models.CharField(max_length=150)),
                ('Durattion', models.CharField(max_length=150)),
            ],
        ),
    ]