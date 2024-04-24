from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name
