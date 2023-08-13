from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    fieldsets=(
        *UserAdmin.fieldsets,
        (
            'Use role',
            {
                'fields':
                (
                    'is_director',
                    'is_producer',
                )
            }
        )
    )
admin.site.register(CustomUser,CustomUserAdmin)