import json
from django.db import models


class Tobacco(models.Model):

    TASTES = (
        ('MINT', 'Mint'),
        ('PIN', 'Pin'),
    )

    TobaccoId = models.IntegerField(auto_created=True, primary_key=True)
    Mark = models.CharField(max_length=32)
    Taste = models.CharField(max_length=32, choices=TASTES)


class Recipe(models.Model):

    LIQUIDS = (
        ('MILK', 'Milk'),
        ('WATER', 'Water'),
    )

    RecipeId = models.IntegerField(auto_created=True, primary_key=True)
    TobaccoList = models.ManyToManyField(Tobacco)
    Optional = models.ManyToManyField(Tobacco, blank=True)
    Flask = models.CharField(max_length=32, choices=LIQUIDS)
    Description = models.TextField(max_length=128)
