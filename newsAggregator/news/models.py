from decimal import MAX_EMAX
from pyexpat import model
from django.db import models

# Create your models here.
class NewsAggre(models.Model):
    NEWS_CATEGORY = (
        ('P','Politics'),
        ('S','Sports'),
        ('H','Health'),
    )

    news_headline = models.CharField(max_length=300,unique=True)
    href_link = models.URLField(max_length=300)
    news_category = models.CharField(max_length=1,choices=NEWS_CATEGORY)

    def __str__(self):
        return self.news_headlines