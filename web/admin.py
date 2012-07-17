from django.contrib import admin
from web.models import *

class BannerAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'type')
admin.site.register(Banner, BannerAdmin)

class PageAdmin(admin.ModelAdmin):
    search_fields = ['page']
    list_display = ('page', 'title',)
admin.site.register(Page, PageAdmin)
