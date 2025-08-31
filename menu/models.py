from django.db import models

class Category(models.Model):


    name = models.CharField(max_length=100, unique=True,verbose_name='نام')

    image = models.ImageField(upload_to="category_images/", blank=True, null=True,verbose_name='تصویر')  # اضافه کردن فیلد تصویر
    class Meta:

        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی"

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items",verbose_name='انتخاب دسته بندی')
    name = models.CharField(max_length=200,verbose_name='نام')
    image = models.ImageField(upload_to="menu_images/",verbose_name='تصویر')
    price = models.DecimalField(max_digits=6, decimal_places=3,verbose_name='قیمت')
    description = models.TextField(blank=True,verbose_name='توضیحات (ترکیبات ، خواص وغیره به انتخاب مدیر)')


    class Meta:

        verbose_name = "منو"
        verbose_name_plural = "منو"
    def __str__(self):
        return self.name
