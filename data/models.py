from django.db import models

# Create your models here.
class Country(models.Model):
  country = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  class Meta:
          ordering = ('country',)
  def __str__(self):
    return self.country
