
from django.db import models

# Create your models here.
class NewsAggre(models.Model):
    NEWS_CATEGORY = (
        ('P','Politics'),
        ('S','Sports'),
        ('H','Health'),
        ('B','Business'),
        ('E','Environment'),
        ('O','Others'),
        ('T','Technology'),
        ('R','Random'),
    )

    news_headline = models.CharField(max_length=300)
    href_link = models.URLField(max_length=300)
    image_link = models.URLField(max_length=300)
    news_descriptions = models.CharField(max_length=500)
    news_category = models.CharField(max_length=1,choices=NEWS_CATEGORY)
    aggregated_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.news_headline