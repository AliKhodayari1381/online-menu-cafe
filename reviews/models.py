from django.db import models
from django_jalali.db import models as jmodels

class Review(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'تعلیق',
        PUBLISHED = 'PB','انتشار'
        REJECTED = 'RJ', 'رد کردن نظر'

    status = models.CharField(max_length=2,choices=Status.choices, default=Status.DRAFT,verbose_name='وضعیت')
    name = models.CharField(max_length=100,verbose_name='نام')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)],verbose_name='امتیاز')
    comment = models.TextField(verbose_name='نظر شما')
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    objects = jmodels.jManager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

        verbose_name='نظر ها'
        verbose_name_plural='نظر ها'


    def __str__(self):
        return f"{self.name} - {self.rating}⭐"
