from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    #control what we see in admin panel
    list_display = ['email', 'username', 'age', 'is_host', 'is_staff',]
    list_editable = ['is_host',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age','is_host', 'slug',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', 'is_host', 'slug', )}),)

admin.site.register(CustomUser, CustomUserAdmin)