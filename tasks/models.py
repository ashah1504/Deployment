from django.db import models


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tasks"
