# Generated by Django 2.0 on 2018-07-20 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTOCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OTMCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='mtocreation',
            name='otm_Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.OTMCreator'),
        ),
    ]
