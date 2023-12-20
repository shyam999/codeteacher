from django.contrib import admin
from .models import Language, Course, Module

admin.site.index_template = 'memcache_status/admin_index.html'

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'created']
    list_filter = ['created', 'language']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
