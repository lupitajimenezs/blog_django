from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)