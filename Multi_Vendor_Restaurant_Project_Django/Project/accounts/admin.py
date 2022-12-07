from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserChangeForm

# Register your models here.

# class MyUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User

class CustomUserAdmin(UserAdmin):
    # form: MyUserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('email',)}),
    # )
    fieldsets = ()



admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
