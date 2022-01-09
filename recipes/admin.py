from django.contrib.admin.helpers import InlineAdminForm
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db.models import fields

# Register your models here.


from .models import Recipe, RecipeIngredient

# User = get_user_model()


class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    extra=0
    readonly_fields = ['quantity_as_float']
    #fields = ['name', 'quantity', 'quantity_as_float','unit','directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    list_display = ['id','name', 'user']
    readonly_fields = ['updated', 'timestamp']
    search_fields = ['name','user']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)