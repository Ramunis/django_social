# Generated by Django 4.0.3 on 2022-04-11 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('ey', models.DateField()),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.spec')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un', models.CharField(max_length=60)),
                ('ey', models.DateField()),
                ('f', models.CharField(max_length=60)),
                ('i', models.CharField(max_length=60)),
                ('o', models.CharField(max_length=60)),
                ('dr', models.DateField()),
                ('male', models.CharField(max_length=20)),
                ('family', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=60)),
                ('pic', models.CharField(max_length=2000)),
                ('phone', models.CharField(max_length=20)),
                ('skype', models.CharField(max_length=60)),
                ('telegram', models.CharField(max_length=60)),
                ('discord', models.CharField(max_length=60)),
                ('google', models.CharField(max_length=60)),
                ('lang', models.TextField()),
                ('about', models.TextField()),
                ('activity', models.TextField()),
                ('interest', models.TextField()),
                ('music', models.TextField()),
                ('films', models.TextField()),
                ('books', models.TextField()),
                ('games', models.TextField()),
                ('fac', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.fac')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.group')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.spec')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slave', models.CharField(max_length=60)),
                ('ds', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student')),
            ],
        ),
    ]