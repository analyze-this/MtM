from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, WorkGroups, WorkTypes, ControlStage, ScopeOfControl, ControlMethod, ControlTypes


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username']


class WorkGroupsAdmin(admin.ModelAdmin):
	list_display = ('id', 'work_group', )
	list_display_links = ('work_group', )


class WorkTypesAdmin(admin.ModelAdmin):
	list_display = ('id', 'work_type', 'work_group', )
	list_display_links = ('id', 'work_type', )


class ControlStageAdmin(admin.ModelAdmin):
	list_display = ('id', 'control_stage', )
	list_display_links = ('control_stage', )


class ScopeOfControlAdmin(admin.ModelAdmin):
	list_display = ('id', 'scope_of_control', )
	list_display_links = ('id', 'scope_of_control')


class ControlMethodAdmin(admin.ModelAdmin):
	list_display = ('id', 'control_method', )
	list_display_links = ('control_method', )


class ControlTypesAdmin(admin.ModelAdmin):
	list_display = ('id', 'number', 'control_stage', 'scope_of_control', 'control_method')
	list_display_links = ('id', 'number', )


admin.site.register(WorkGroups, WorkGroupsAdmin)
admin.site.register(WorkTypes, WorkTypesAdmin)
admin.site.register(ControlStage, ControlStageAdmin)
admin.site.register(ScopeOfControl, ScopeOfControlAdmin)
admin.site.register(ControlMethod, ControlMethodAdmin)
admin.site.register(ControlTypes, ControlTypesAdmin)



