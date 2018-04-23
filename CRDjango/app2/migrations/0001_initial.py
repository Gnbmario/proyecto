# Generated by Django 2.0.4 on 2018-04-23 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('address', models.CharField(max_length=250, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.School', verbose_name='Escuela')),
            ],
        ),
    ]
