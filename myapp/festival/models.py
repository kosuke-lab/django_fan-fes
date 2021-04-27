from django.db import models
from django.utils import timezone
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse

class Country(models.Model):
    country = models.CharField(
        '国名',
        max_length=255
    )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.country

    
class Area(models.Model):
    area = models.CharField(
        'エリア',
        max_length=225,
        blank = False,
        unique = True,
    )

    url_code = models.CharField(
        'URL名',
        max_length = 50,
        blank = False,
        unique = True,
    )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.area


class Festival(models.Model):
    name = models.CharField(
        'お祭りの名前',
        max_length=200
        )

    area = models.ForeignKey(
    Area,
    verbose_name = 'エリア',
    on_delete=models.PROTECT,
        )

    country = models.ForeignKey(
    Country,
    verbose_name = '国名',
    on_delete=models.PROTECT,
         )
    
    location = models.CharField(
        '地名',
        max_length=200,
         null =True
         )
    start_time = models.CharField(
        '開催日',
        max_length=200,
        null=True
        )

    thumbnail = models.ImageField(
        'サムネイル',
        upload_to = 'img/',
        default='img/no_image.jpeg'
        )
        
    pc_thumbnail = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 60}
        )
    
    detail_thumbnail = ImageSpecField(
        source='thumbnail',
        processors=[ResizeToFill(445, 329)],
        format='webp',
        options={'quality': 60}
    )

    regist_date = models.DateField(
        '投稿日',
        default=datetime.now
        )
    detail =models.TextField(
            'お祭りの詳細（400文字以内）',
            max_length = 400,
        )
    
    author = models.ForeignKey(
        'auth.User',
        verbose_name = '作成者',
        on_delete=models.CASCADE,
    )
    views = models.PositiveIntegerField(
        default = 0,
    )


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('festival:detail', kwargs={
            'url_code': self.area.url_code,
            'pk': self.pk}
            )


class Comment(models.Model):
    text = models.TextField(
        max_length = 400,
        verbose_name = 'コメント欄', 
    )
    post_time = models.DateField(
        auto_now = True,
        )
    article = models.ForeignKey(
        Festival,
        verbose_name = 'お祭り名', 
        related_name='comments',
        on_delete=models.CASCADE,
    )
    author = models.CharField(
        max_length = 200,
        verbose_name = '名前', 
    )

    def __str__(self):
         return self.text
    


