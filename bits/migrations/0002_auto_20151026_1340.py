# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='pivacy',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'All'), (b'I', b'I'), (b'F', b'Followers')]),
        ),
    ]
