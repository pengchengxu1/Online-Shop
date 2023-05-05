from django.contrib import admin
from goods.models import GoodType,Good


class GoodTypeAdmin(admin.ModelAdmin):
    # 列表中的列
    list_display = ['id', 'name', 'create_time', 'update_time']
    # 搜索框
    search_fields = ['name', 'create_time', 'update_time']


class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'good_type', 'inventory', 'price',
                    'create_time', 'update_time']
    # 搜索框
    search_fields = ['id', 'title', 'good_type', 'price']


admin.site.register(GoodType, GoodTypeAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.site_header = 'Sales Management System'

admin.site.site_title = 'Sales Management System'
