from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bit(models.Model):
    bit_text = models.CharField(max_length=200)
    bit_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, related_name='author')
    o_author = models.ForeignKey(User, related_name='o_author')
    priv_options = (
        ('A', 'All'),
        ('I', 'I'),
        ('F', 'Followers'),
    )
    pivacy = models.CharField(max_length=1, choices=priv_options, default='A')
