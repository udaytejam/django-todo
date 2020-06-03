from django.contrib import admin

# Register your models here.
from .models import TodoItem

admin.site.site_header = 'ToDoApp Admin'
admin.site.site_title = 'ToDoApp Administration'
admin.site.index_title = 'ToDoApp Administration'

# admin.site.register(TodoItem)

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    pass