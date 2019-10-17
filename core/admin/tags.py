from django.contrib import admin

from ..models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "tag")


admin.site.register(Tag, TagAdmin)
