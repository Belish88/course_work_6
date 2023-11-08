from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'surname', 'name', 'patronymic')
    list_filter = ('email',)
    search_fields = ('email', 'surname')
