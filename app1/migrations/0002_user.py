# Generated by Django 2.0.2 on 2018-03-06 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app1.Webpage')),
            ],
        ),
    ]
