# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('limit', models.IntegerField()),
                ('status', models.BooleanField()),
                ('address', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name=b'events time')),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=75)),
                ('sign', models.BooleanField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='sign.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
