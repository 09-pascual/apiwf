from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from workflowapiapi.views import (
    UserViewSet, ClientViewSet, ProjectViewSet,
    WorkerViewSet, GroupViewSet, ProjectWorkerViewSet,
    GroupWorkerViewSet, ProjectGroupViewSet,
    register_user, login_user
)

router = routers.DefaultRouter(trailing_slash=False)

# Register viewsets
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'projectworkers', ProjectWorkerViewSet)
router.register(r'groupworkers', GroupWorkerViewSet)
router.register(r'projectgroups', ProjectGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth', obtain_auth_token),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)