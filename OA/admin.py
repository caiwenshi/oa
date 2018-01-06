from django.contrib import admin
from .models import *

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_cn', 'gender', 'loc')
    list_filter = ('gender', 'loc')
    ordering = ('join_date', 'birthday')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'team', 'start_date', 'end_date')
    ordering = ('code', 'start_date')


class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('emp_order', 'emp_name', 'role')
    list_filter = ('emp_order', 'role')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(EmployeeProject, EmployeeProjectAdmin)
