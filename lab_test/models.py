from django.db import models

class LabTest(models.Model):
    price = models.CharField(max_length=50)

