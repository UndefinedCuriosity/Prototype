from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    #description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #        return self.document    
    #def get_absolute_url(self):
    #    return "/documents/%s" % self.slug
    class Meta:
        ordering = ['-uploaded_at']
