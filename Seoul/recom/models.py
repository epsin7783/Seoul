from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class recommend(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    addr = models.CharField(max_length=255, null=False)
    grade = models.FloatField(validators=[MinValueValidator(0,5),MaxValueValidator(5.0)])
    review = models.TextField(null=False)