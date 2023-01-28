from django.contrib import admin
from .models import *
# Register your models here.

class AyahAdmin(admin.StackedInline):
	model =  Ayah

@admin.register(Surai)
class SuraiAdmin(admin.ModelAdmin):
	inlines = [AyahAdmin]
	list_display = ['id','number','name_ar', 'name_en']

admin.site.register(Ayah)
