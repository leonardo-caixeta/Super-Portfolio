from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            profile_id = kwargs.get('pk')
            profile = Profile.objects.get(pk=profile_id)
            context = {'profile': profile}
            return render(request, 'profile_detail.html', context)
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
