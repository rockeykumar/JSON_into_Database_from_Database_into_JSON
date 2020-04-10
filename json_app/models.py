from django.db import models

# Create your models here.

class json_table(models.Model):
    name = models.CharField(max_length=2000)
    json_item = models.CharField(max_length=2000)

    def __str__(self):
        return self.name