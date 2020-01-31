import json
from django.db import models


class Tobacco(models.Model):

    TobaccoId = models.IntegerField(auto_created=True, primary_key=True)
    Mark = models.CharField(max_length=32)
    Taste = models.CharField(max_length=32)


class Recipe(models.Model):

    LIQUIDS = (
        ('MILK', 'milk'),
        ('WATER', 'water'),
        ('GREEN TEA', 'green tea'),
        ('ICE', 'ice'),
    )
    
    RecipeId = models.IntegerField(auto_created=True, primary_key=True)
    TobaccoList = models.ManyToManyField(Tobacco,related_name="tobacco")
    OptionalList = models.ManyToManyField(Tobacco, blank=True,related_name="optional")
    Flask = models.CharField(max_length=32, choices=LIQUIDS)
    Description = models.TextField(max_length=128)
