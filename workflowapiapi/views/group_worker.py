from rest_framework import viewsets, serializers
from workflowapiapi.models import GroupWorker

class GroupWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWorker
        fields = ['id', 'group', 'worker']

class GroupWorkerViewSet(viewsets.ModelViewSet):
    queryset = GroupWorker.objects.all()
    serializer_class = GroupWorkerSerializer