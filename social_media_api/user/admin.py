
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Optionally, customize fields displayed in admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'bio', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'bio', 'profile_picture')}),
    )
    list_display = UserAdmin.list_display + ('phone_number', 'bio', 'profile_picture')
    search_fields = ('email', 'username', 'phone_number', 'bio')
    ordering = ('email',)
    list_editable = ('phone_number', 'bio', 'profile_picture')