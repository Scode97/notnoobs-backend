# Generated by Django 2.1.1 on 2018-09-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20180924_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subCategory', models.ManyToManyField(to='feed.Category')),
            ],
        ),
        migrations.RenameModel(
            old_name='PhysicalActivities',
            new_name='PhysicalActivity',
        ),
    ]
