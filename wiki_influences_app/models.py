from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=512, unique=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=256, blank=True, null=True)
    influences = models.ManyToManyField("self", blank=True, null=True, related_name='influenced')

    def __str__(self):
        return self.name
