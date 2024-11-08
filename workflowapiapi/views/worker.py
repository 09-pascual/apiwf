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

class WorkerCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'user', 'availability_status']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(  # Use create_user instead of create
            username=user_data['username'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            birth_date=user_data['birth_date'],
            phone_number=user_data['phone_number'],
            nickname=user_data['nickname'],
            role='worker'  # Set role explicitly
        )
        
        # Create and return Worker instance
        worker = Worker.objects.create(user=user, **validated_data)
        return worker

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return WorkerCreateSerializer
        if self.action in ['update', 'partial_update']:
            return WorkerWriteSerializer
        return WorkerReadSerializer