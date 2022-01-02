from rest_framework import serializers
from .models import user, submissions


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = submissions
        fields = "__all__"
