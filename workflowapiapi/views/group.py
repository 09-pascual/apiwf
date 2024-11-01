from rest_framework import viewsets, serializers
from workflowapiapi.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description']
        # Note: 'workers' and 'projects' will be handled through junction tables

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer