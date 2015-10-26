# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bit_text', models.CharField(max_length=200)),
                ('bit_date', models.DateTimeField(verbose_name=b'date published')),
                ('pivacy', models.CharField(max_length=1, choices=[(b'A', b'All'), (b'I', b'I'), (b'F', b'Followers')])),
                ('author', models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL)),
                ('o_author', models.ForeignKey(related_name='o_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
