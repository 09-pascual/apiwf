from rest_framework import viewsets, serializers
from workflowapiapi.models import ProjectGroup
from .group import GroupSerializer

class ProjectGroupReadSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    
    class Meta:
        model = ProjectGroup
        fields = ['id', 'group', 'project']

class ProjectGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGroup
        fields = ['id', 'group', 'project']
        
class ProjectGroupViewSet(viewsets.ModelViewSet):
    queryset = ProjectGroup.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # When reading data
            return ProjectGroupReadSerializer
        return ProjectGroupSerializer