# Generated by Django 3.0.5 on 2020-05-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='images/')),
                ('author', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
