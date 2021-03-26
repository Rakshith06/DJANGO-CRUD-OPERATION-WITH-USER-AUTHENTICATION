from django.contrib import admin


from myapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    l=['eno','ename','esal','eadd']
admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
