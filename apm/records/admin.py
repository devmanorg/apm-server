from django.contrib import admin

from .models import Play, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    raw_id_fields = ['play']


admin.site.register(Play)