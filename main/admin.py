from django.contrib import admin
from main.models import Genome


class InLine(admin.StackedInline):
    model = Genome


class GenomeAdmin(admin.ModelAdmin):
    inlines = InLine
    readonly_fields = ['sequence']


admin.site.register(Genome)
