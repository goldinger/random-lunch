# Generated by Django 3.0.3 on 2020-02-25 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200219_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.Person')),
                ('person_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.Person')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='couples', to='backend.Session')),
            ],
        ),
    ]
