from django.db import models
# Documentation: https://docs.djangoproject.com/en/5.0/topics/db/models/

class Person(models.Model):
    id_card = models.CharField(primary_key=True, max_length=9, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
