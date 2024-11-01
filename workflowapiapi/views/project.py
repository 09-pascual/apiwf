from rest_framework import viewsets, serializers
from workflowapiapi.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'client', 'name', 'status', 'start_date', 'end_date', 
                 'expected_duration']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
