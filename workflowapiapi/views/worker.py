from rest_framework import viewsets, serializers
from workflowapiapi.models import Worker
from .user import UserSerializer
from .project_worker import ProjectWorkerSerializer
from .group_worker import GroupWorkerSerializer

class WorkerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    projectworker_set = ProjectWorkerSerializer(many=True, read_only=True)
    groupworker_set = GroupWorkerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Worker
        fields = ['id', 'user', 'availability_status', 'projectworker_set', 'groupworker_set']
        # Note: 'projects' will be handled through ProjectWorker

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
