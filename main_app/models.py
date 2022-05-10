from django.db import models

# Create your models here.
class Finch(models.Model):
    #define attributes/fields
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    # Django will create inputs for a form
    # TextField will create a <textarea>
    description = models.TextField(max_length=250)
    age = models.IntegerField()
