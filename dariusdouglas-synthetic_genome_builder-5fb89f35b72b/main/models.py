from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# GENOME CLASS & DATABASE FIELDS
class Genome(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True)
    sequence = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("genome:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp"]
