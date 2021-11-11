from django.shortcuts import render

from rest_framework import generics
from mpiapi0 import serializers
from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

from mpiapi0.models import Post
from rest_framework import permissions
from mpiapi0.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


from mpiapi0.models import Comment

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

from mpiapi0.models import Upvote

'''class UpvoteList(generics.ListCreateAPIView):
    queryset = Upvote.objects.all()
    serializer_class = serializers.UpvoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]'''

from django.http import JsonResponse
'''
def save_upvote(request, pk):
    if request.method == 'POST':
        post_id = request.POST['postid']
        post = Post.objects.get(pk=post_id)
        user = request.user
        check = Upvote.objects.filter(post=post,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            Upvote.objects.create(
                post=post,
                user=user
            )
            return JsonResponse({'bool':True})
'''

from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ActionSerializer, PostSerializer

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def action_view(request, *args, **kwargs):
    '''
    id is required.
    Action options are: like
    '''
    serializer = ActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        post_id = data.get("id")
        action = data.get("action")
        #content = data.get("content")
        qs = Post.objects.filter(id=post_id)
        print(qs)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        print('--- obj: ', obj)
        print('--- obj.upvotes_amount: ', obj.upvotes_amount)
        print('--- request user: ', request.user)
        print('--- admin user: ', User.objects.all().filter(username='admin').first())
        print('======== time: ', Upvote.objects.all().filter(upvoted_on__day=1))
        user = User.objects.all().filter(username='user1').first() # temporar user for testing
        #user = request.user # for production
        if action == "upvote":
            check = Upvote.objects.filter(post=obj,author_name=user).count()
            if check > 0: # check if this upvote exists
                return JsonResponse({'Upvote':'Already exist'})
                ### to unvote     elif action == "unvote":
                '''
                obj.upvotes_amount.remove(request.user)
                Upvote.objects.delete(post=obj, author_name=user)
                serializer = PostSerializer(obj)
                return Response(serializer.data, status=200)
                '''
            else:
                Upvote.objects.create(post=obj, author_name=user)
                serializer = PostSerializer(obj)
                return Response(serializer.data, status=200)
    return Response({}, status=200)


#def delete_everything(self):
#    Reporter.objects.all().delete()

#def drop_table(self):
#    cursor = connection.cursor()
#    table_name = self.model._meta.db_table
#    sql = "DROP TABLE %s;" % (table_name, )
#    cursor.execute(sql)