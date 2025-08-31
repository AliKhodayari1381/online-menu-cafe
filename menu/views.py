from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem

def menu_view(request):
    categories = Category.objects.all()  # دریافت همه دسته‌ها همراه با تصاویرشان
    return render(request, 'menu/menu.html', {'categories': categories})

def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = category.items.all()
    return render(request, 'menu/category_items.html', {'category': category, 'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'menu/item_detail.html', {'item': item})
