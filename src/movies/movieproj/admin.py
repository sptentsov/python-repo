from movieproj.models import User
from django.contrib import admin
from movieproj.models import List

# class ChoiceInline(admin.StackedInline):
    # model = Choice
    # extra = 3

# class PollAdmin(admin.ModelAdmin):
    # fieldsets = [
        # (None,               {'fields': ['question']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]

admin.site.register(User)
admin.site.register(List)