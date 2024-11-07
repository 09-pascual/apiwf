from rest_framework import viewsets, serializers
from workflowapiapi.models import GroupWorker
from .group import GroupSerializer

class GroupWorkerReadSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = GroupWorker
        fields = ['id', 'group', 'worker']

class GroupWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWorker
        fields = ['id', 'group', 'worker']

class GroupWorkerViewSet(viewsets.ModelViewSet):
    queryset = GroupWorker.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GroupWorkerReadSerializer
        return GroupWorkerSerializer