from django.shortcuts import render
from rest_framework import viewsets
from . models import Note
from . serializers import NoteSerializer
from django.contrib.auth.models import User
# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    def perform_update(self,serializer):
        shared_with = self.request.data.get('shared_with')
        instance = serializer.save()
        
        if shared_with:
            instance.shared_with.set(shared_with)
        
    def file_get(self,serializer):
        audio_file = self.request.data.get('audio_file')
        video_file = self.request.data.get('video_file')
        serializer.save(audio_file=audio_file,video_file=video_file)
        
    