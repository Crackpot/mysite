from django.contrib import admin

from .models import Choice, Question, Code
from .form import QuestionForm, ChoiceForm, CodeForm


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class ChoiceAdmin(admin.ModelAdmin):
    form = ChoiceForm
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class CodeAdmin(admin.ModelAdmin):
    form = CodeForm
    list_display = ['id', 'title']


admin.site.register(Code, CodeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
