from django.contrib import admin

# Register your models here.
from .models import Bit


class BitAdmin (admin.ModelAdmin):
    list_display= ('bit_text',)
    search_fields= ['bit_text',]
    list_filter= ('author','pivacy')

admin.site.register(Bit,BitAdmin)
