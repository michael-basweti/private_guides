from rest_framework import generics, status, permissions, mixins, viewsets
from .models import Blog
from .serializers import BlogSerializer
from create_guide_profile.permissions import IsOwnerOrReadOnly


class BlogViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                  viewsets.GenericViewSet
                  ):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)