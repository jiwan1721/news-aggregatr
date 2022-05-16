from . aggregator import NewsAggre
from rest_framework import serializers

class NewsAggreSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAggre
        fields = ['id','news_headline','href_link','image_link','news_category','aggregated_date']