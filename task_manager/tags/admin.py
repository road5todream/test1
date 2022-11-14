from django.contrib import admin
from .models import Tags


class TagsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tags, TagsAdmin)
