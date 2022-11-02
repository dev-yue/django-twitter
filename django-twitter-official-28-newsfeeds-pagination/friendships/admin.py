from django.contrib import admin
from friendships.models import Friendship

认准一手微信study322 其他均为翻录倒卖
九章来offer都有  需要的+我
课程目录
https://www.yuque.com/study001/xk/list

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'created_at')
    date_hierarchy = 'created_at'
