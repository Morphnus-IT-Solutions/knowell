from django.contrib import admin
from web.models import *

class BannerAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title',)
admin.site.register(Banner, BannerAdmin)
