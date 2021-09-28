from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import exceptions

from posts.models import Comment, Group, Post, User

from . import serializers as s
from .permissions import IsAuthentAndAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = s.PostSerializer
    permission_classes = (IsAuthentAndAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = s.GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = s.CommentSerializer
    permission_classes = (IsAuthentAndAuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        new_queryset = Comment.objects.filter(post=post)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = s.FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        new_queryset = self.request.user.user.all()
        return new_queryset

    def perform_create(self, serializer):
        following = get_object_or_404(
            User,
            username=self.request.data['following']
        )
        user = self.request.user
        if user == following:
            raise exceptions.ValidationError(
                'Вы пытаетесь подписаться на себя'
            )
        serializer.save(user=user, following=following)
