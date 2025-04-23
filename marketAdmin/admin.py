from django.contrib import admin
from .models import medicines, health



# Register your models here.
@admin.register(medicines)
class medicinesAdmin(admin.ModelAdmin):
    list_display = ['id','mname','mprice','minfo','mamm','mimg']


@admin.register(health)
class healthAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hprice','hinfo','hamm','himg']