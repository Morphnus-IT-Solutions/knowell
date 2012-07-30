from django.contrib import admin
from question.models import *

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question']
    list_display = ('question', 'section', 'level_of_difficulty', 'score',)
    list_filter = ('section__name', 'level_of_difficulty__level')
    inlines = [OptionInline]
admin.site.register(Question, QuestionAdmin)
