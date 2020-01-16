from django.contrib import admin

# Register your models here.
from users.models import UserInfo,UserToken

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username',)

