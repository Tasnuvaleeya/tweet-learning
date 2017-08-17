from django.utils.timesince import timesince
from rest_framework import serializers
from tweet_feed.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer):
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"