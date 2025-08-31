from django.contrib import admin
from .models import Category, MenuItem

admin.sites.AdminSite.site_header= "پنل مدیریت کافه"
admin.sites.AdminSite.site_title= "پنل "
admin.sites.AdminSite.index_title= "پنل مدیریت"


admin.site.register(Category)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'price']
    search_fields=['category__name','name', 'price','description']
