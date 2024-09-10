from django.contrib import admin
from .models import Employee, Department, Role, Profile, Attendance, LeaveRequest

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)
@admin.register(Profile)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'role')
    search_fields = ('user__username', 'company__name', 'role')
    list_filter = ('company', 'role')
admin.site.register(Attendance)
admin.site.register(LeaveRequest)