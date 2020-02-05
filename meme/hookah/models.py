from django.db import models


class Tabacco(models.Model):

    TobaccoId = models.IntegerField(auto_created=True, primary_key=True)
    Mark = models.CharField(max_length=32,null=True )
    Taste = models.CharField(max_length=32)

    def __str__(self):
        return f'Taste: {self.Taste} {"Taste: " + self.Mark if self.Mark else ""}' 

class Recipe(models.Model):

    LIQUIDS = (
        ('MILK', 'milk'),
        ('WATER', 'water'),
        ('GREEN TEA', 'green tea'),
        ('ICE', 'ice'),
    )
    
    RecipeId = models.IntegerField(auto_created=True, primary_key=True)
    TabaccoList = models.ManyToManyField(Tabacco,related_name="TabaccoList")
    OptionalList = models.ManyToManyField(Tabacco, blank=True,related_name="OptionalList")
    Flask = models.CharField(max_length=32, choices=LIQUIDS)
    Description = models.TextField(max_length=128)

    def __str__(self):
        return str(self.RecipeId) + ' ' + ' '.join(self.TabaccoList)