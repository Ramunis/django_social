# Generated by Django 4.0.3 on 2022-04-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_board_community_theme_post_pli_pcom_member_like_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('img', models.CharField(max_length=2000)),
                ('dp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('about', models.TextField()),
                ('de', models.DateField()),
                ('adr', models.CharField(max_length=100)),
                ('sp', models.CharField(max_length=100)),
                ('dc', models.DateField()),
                ('site', models.CharField(max_length=60)),
                ('mail', models.CharField(max_length=60)),
                ('telegram', models.CharField(max_length=60)),
                ('pic', models.CharField(max_length=2000)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.event')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Eli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dl', models.DateField()),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.advert')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Ecom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com', models.TextField()),
                ('dl', models.DateField()),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.advert')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student')),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.event'),
        ),
        migrations.AddField(
            model_name='advert',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.student'),
        ),
    ]
