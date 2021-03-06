# Generated by Django 2.1.1 on 2018-09-24 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20180924_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('category', models.ManyToManyField(to='feed.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='quest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Question'),
        ),
    ]
