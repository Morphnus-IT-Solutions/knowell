from django.contrib import admin
from question.models import *

class CharacteristicsInline(admin.TabularInline):
    model = Characteristics
    extra = 0

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question']
    list_display = ('question', 'section', 'level_of_difficulty', 'score',)
    list_filter = ('section__name', 'level_of_difficulty__level')
    inlines = [CharacteristicsInline, OptionInline]
admin.site.register(Question, QuestionAdmin)
