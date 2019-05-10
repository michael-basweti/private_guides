from rest_framework import generics, status, permissions, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Image, Video, Review
from .serializers import ProfileSerializer, ImageSerializer, VideoSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser, FormParser

def current_profile(request):
    authenticated_user=request.user
    return authenticated_user.profile

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

class UserProfile(viewsets.ModelViewSet):
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Profile.objects.filter(user=user)
    
    
class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    

    def perform_create(self, serializer):
         serializer.save(user=self.request.user,
         image_url=self.request.data.get('image_url'))


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

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)


class ReviewViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                  viewsets.GenericViewSet
                  ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)