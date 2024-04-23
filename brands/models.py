from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name
