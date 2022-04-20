from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
	list_display = ['username','user_type']

@admin.register(Student)
class StudAdmin(ImportExportModelAdmin):
	pass
admin.site.register(CustomerUser,UserModel)
admin.site.register(Cours)
admin.site.register(Session_year)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Notif_Staff)
admin.site.register(Staff_Leave)
admin.site.register(Staff_Feedback)
admin.site.register(Notif_Stud)
admin.site.register(Stud_Feedback)
admin.site.register(Attendance_report)
admin.site.register(Attendance)
admin.site.register(StudResult)