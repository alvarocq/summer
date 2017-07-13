# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=160)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.author + ": " +self.body[:30]

# Create your models here.
