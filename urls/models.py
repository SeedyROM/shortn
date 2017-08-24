from django.db import models

from django.utils.crypto import get_random_string

class Url(models.Model):
    url = models.URLField()
    tiny_url = models.CharField(max_length=9, unique=True)
    clicks = models.PositiveIntegerField(default=0)


    def save(self, *args, **kwargs):
        if not self.id:
            self.tiny_url = get_random_string(length=9)

        return super(Url, self).save(*args, **kwargs)

class Analytic(models.Model):
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    url = models.ForeignKey(Url, related_name='analytics')
    referrer = models.URLField(blank=True, null=True)
