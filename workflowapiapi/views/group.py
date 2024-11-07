from rest_framework import viewsets, serializers
from workflowapiapi.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'groupworker_set', 'projectgroup_set']
        depth = 2  # This will automatically serialize nested relationships up to 2 levels deep

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer