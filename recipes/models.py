import re
from django.db import models
from django.urls import reverse

from django.conf import settings

import pint
from pint import measurement

# Create your models here.
from .utils import number_str_to_float
from .validators import  validate_unit_of_measure

"""
- Global 
    - Ingredients
    - Recipes
- User
    - Ingredients
    - Recipes
        - ingredients
        - Directions for ingredients
"""

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id":self.id})

    def __str__(self):
        return(self.name+'('+str(self.id)+')')

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    quantity =  models.CharField(max_length=50) 
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50,validators=[validate_unit_of_measure])
    directions = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def convert_to_system(self,system="mks"):
        if self.quantity_as_float is None:
            return None  
        ureg = pint.UnitRegistry(system=system)
        measurement =  self.quantity_as_float * ureg[self.unit]
        return measurement

   

    def as_mks(self):
        #meter, quilogram, secodns
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()

    def as_imperial(self):
        #miles, pounds, seconds
        measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()
        


    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            quantity_as_float = None
        super().save(*args,**kwargs)

    def __str__(self):
        return(self.name+'('+str(self.id)+')')

# class RecipeImage(models.Model):
#     recipe = models.ForeignKey(Recipe)
#     description = 