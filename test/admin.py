from django.contrib import admin
from test.models import *


class LevelOfDifficultyAdmin(admin.ModelAdmin):
    search_fields = ['level']
    list_display = ('level',)
admin.site.register(LevelOfDifficulty, LevelOfDifficultyAdmin)

class SectionGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    list_filter = ('name',)
admin.site.register(SectionGroup, SectionGroupAdmin)

class SectionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'group', 'type',)
    list_filter = ('group__name',)
admin.site.register(Section, SectionAdmin)

class TestSectionsInline(admin.TabularInline):
    model = TestSections
    extra = 3

class TestAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'marks', 'time', )
    list_filter = ('standard__standard',)
    inlines = [TestSectionsInline]
admin.site.register(Test, TestAdmin)
