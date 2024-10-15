from django.contrib import admin
from .models import Category, Pizza

admin.site.empty_value_display = 'Не задано'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'output_order',
        'is_published'
    )
    list_editable = (
        'output_order',
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


class PizzaAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'structure',
        'size',
        'description',
        'price',
        'output_order',
        'is_published',
        'is_on_main',
        '_meta',
    )
    list_editable = (
        'structure',
        'description',
        'size',
        'price',
        'output_order',
        'is_published',
        'is_on_main',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)

    def _meta(self, row):
        return ', '.join([x.title for x in row.category.all()])


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Category, CategoryAdmin)
