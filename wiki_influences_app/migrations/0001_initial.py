# Generated by Django 3.0 on 2019-12-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=256, null=True)),
                ('influences', models.ManyToManyField(blank=True, null=True, related_name='_person_influences_+', to='wiki_influences_app.Person')),
            ],
        ),
    ]
