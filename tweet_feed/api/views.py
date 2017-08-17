from rest_framework import generics
from .seriazilers import TweetModelSerializer
from tweet_feed.models import Tweet
from rest_framework import permissions


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tweet.objects.all()