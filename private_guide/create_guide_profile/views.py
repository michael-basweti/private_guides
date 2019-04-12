from rest_framework import generics, status, permissions, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Image, Video
from .serializers import ProfileSerializer, ImageSerializer, VideoSerializer
from .permissions import IsOwnerOrReadOnly


# class ProfileView(APIView):
#     #Allow any user to hit this endpoint
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#     # renderer_classes = (ProfileJSONRenderer,)

#     def get(self, request, user_id, format=None):
#         try:
#             profile =  Profile.objects.get(user__id=user_id)
#             serializer = ProfileSerializer(profile, context={'request': request})
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Profile.DoesNotExist:
#             return Response(
#                 {
#                     'message': 'Profile not found'
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )

#     def put(self, request, user_id, format=None):
#         try:
#             serializer_data = request.data.get('user', {})
#             serializer = ProfileSerializer(
#                 request.user.profile,
#                 data=serializer_data,
#                 partial=True,
#                 context={'request': request}
#             )
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         except Profile.DoesNotExist:
#             return Response(
#                     {
#                         'message': 'Profile not found'
#                     },
#                     status=status.HTTP_404_NOT_FOUND
#                 )

class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class VideoView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)