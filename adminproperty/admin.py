from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import AdminProperty

class AdminPropertyAdmin(admin.ModelAdmin):
    list_display = ('admin', 'first_name', 'last_name','gender', 'age', 'display_birthday','email', )
    search_fields = ('username', 'first_name', 'last_name','email')
    list_filter = ('groups',)
    exclude = ('username', 'password', 'is_staff', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions', 'is_superuser')

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return False

    def queryset(self, request):
        qs = super(AdminPropertyAdmin, self).queryset(request)
        return qs if request.user.is_superuser else qs.filter(admin=request.user)



#UserAdmin.list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined',)
admin.site.register(AdminProperty, AdminPropertyAdmin)
#admin.site.unregister(User)
#admin.site.register(User,UserAdmin)
