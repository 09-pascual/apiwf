from rest_framework import viewsets, serializers
from workflowapiapi.models import ProjectWorker

class ProjectWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectWorker
        fields = ['id', 'worker', 'project']

class ProjectWorkerViewSet(viewsets.ModelViewSet):
    queryset = ProjectWorker.objects.all()
    serializer_class = ProjectWorkerSerializer