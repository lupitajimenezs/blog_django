from rest_framework import serializers
from comments.models import Comments

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'content',
            'created_at',
            'user',
            'posts'
        ]