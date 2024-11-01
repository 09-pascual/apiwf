from rest_framework import viewsets, serializers
from workflowapiapi.models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'user', 'availability_status']
        # Note: 'projects' will be handled through ProjectWorker

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
