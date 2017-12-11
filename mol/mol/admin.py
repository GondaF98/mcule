from django.contrib import admin

from . import models


class ComponentRelationInline(admin.StackedInline):
    pass


class CompoundAdmin(admin.ModelAdmin):
    list_display = (
        "smiles",
        )
    inlines = []


class ComponentRelationAdmin(admin.ModelAdmin):
    list_display = (
        "parent", "component", "multiplicity",
        )


admin.site.register(models.Compound, CompoundAdmin)
admin.site.register(models.ComponentRelation, ComponentRelationAdmin)
