# Generated by Django 3.2.11 on 2022-01-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_auto_20220130_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='participents',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.Participent'),
        ),
    ]
