from rest_framework import serializers
from . models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    audio_file = serializers.FileField(required = False, allow_null = True)
    video_file = serializers.FileField(required = False, allow_null = True)
    shared_with = serializers.PrimaryKeyRelatedField(many=True,queryset = User.objects.all(),required = False)
    class Meta:
        model = Note
        fields = '__all__'