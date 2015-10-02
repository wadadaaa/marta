from django.contrib import admin

# Register your models here.

from section.models import Section

class SectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Section, SectionAdmin)
