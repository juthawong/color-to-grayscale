from django.db import models


class Image(models.Model):
    color_file = models.ImageField()
    gray_file = models.ImageField(blank=True, null=True)
