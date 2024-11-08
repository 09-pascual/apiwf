from rest_framework import viewsets, serializers
from workflowapiapi.models import Worker, User
from .user import UserSerializer



  
class WorkerReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'user', 'availability_status'] 
        
class WorkerWriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'user', 'availability_status']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        # Update User instance
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()
        
        # Update Worker instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WorkerWriteSerializer
        return WorkerReadSerializer