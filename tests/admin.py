#from django.contrib import admin
#from tests.models import *
#
#
#class LevelOfDifficultyAdmin(admin.ModelAdmin):
#    list_display = ('level',)
#admin.site.register(LevelOfDifficulty, LevelOfDifficultyAdmin)
#
#
#class SectionAdmin(admin.ModelAdmin):
#    search_fields = ['name']
#    list_display = ('name', 'type',)
#    list_filter = ('name',)
#admin.site.register(Section, SectionAdmin)
#
#class TestSectionsInline(admin.TabularInline):
#    model = TestSections
#    extra = 3
#
#class Test(admin.ModelAdmin):
#    search_fields = ['title', 'standard__standard']
#    list_display = ('title', 'marks', 'time', 'stardard', )
#    list_filter = ('standard__standard',)
#    inlines = [TestSectionsInline]
#admin.site.register(Test, TestAdmin)
