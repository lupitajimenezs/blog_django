from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.models import Comments
from comments.api.serializers import CommentsSerializers
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentsApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    filter_backends = [OrderingFilter]
    ordering = ['-create_at'] #Ordenando de manera descendente
    filterset_fields = ['post']