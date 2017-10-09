"""This module."""

from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ This class"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        """ Method publish."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
