from django.db import models

class Laboratorio(models.Model):
    name = models.CharField(max_length=200, verbose_name='Labs Name')
    location = models.CharField(max_length=200, verbose_name='Location')

    def __str__(self):
        return self.name
