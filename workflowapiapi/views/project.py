from rest_framework import viewsets, serializers
from workflowapiapi.models import Project
from .client import ClientSerializer
from .project_group import ProjectGroupReadSerializer

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()  
    projectgroup_set =  ProjectGroupReadSerializer(many=True, read_only=True) 

    class Meta:
        model = Project
        fields = ['id', 'client', 'name', 'status', 'start_date', 'end_date', 
                 'expected_duration', 'projectgroup_set']
        
class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'client', 'name', 'status', 'start_date', 'end_date',
                 'expected_duration']
        
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectWriteSerializer
        return ProjectSerializer