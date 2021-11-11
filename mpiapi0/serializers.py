from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

from mpiapi0.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author_name.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #upvotes_amount = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    upvotes_amount = serializers.SerializerMethodField(read_only=True)
    
    def get_upvotes_amount(self, obj):
        return obj.upvotes_amount.count()
    #def get_upvotes_amount(self, post):
    #    return post.upvotes.count()

    class Meta:
        model = Post
        fields = ['id', 'title', 'creation_date', 'upvotes_amount', 'content', 'author_name', 'comments']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']
    
class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author_name.username')

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'creation_date', 'post']

from django.conf import settings

ACTION_OPTIONS = settings.ACTION_OPTIONS

class ActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    #content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip() # "Upvote " => "upvote"
        if not value in ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action")
        return value