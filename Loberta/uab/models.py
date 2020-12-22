from django.db import models


class URLs(models.Model):
    url_name = models.URLField(verbose_name='URL name')

    class Meta:
        verbose_name = 'URL'

    def __str__(self):
        return self.url_name

