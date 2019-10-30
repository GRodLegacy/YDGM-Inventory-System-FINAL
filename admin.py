from django.contrib import admin
from .models import Electronics, Apparel, Equipment, Toys, Footwear

# Register your models here.

@admin.register(Electronics, Apparel, Equipment, Toys, Footwear)
class ViewAdmin(admin.ModelAdmin):
    pass