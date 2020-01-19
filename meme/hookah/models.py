from django.db import models
import json

class Tobacco(models.Model):

    TASTES = (
        ('MINT', 'Mint'),
        ('PIN', 'Pin'),

    )

    def __readMixes__():
        with open('mixes.txt','r') as f:
            data = json.load(f)

    index = models.IntegerField(auto_created=True, primary_key=True)
    mark = models.CharField(max_length=30)
    taste = models.CharField(max_length=30, choices=TASTES)