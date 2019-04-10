from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from .models import Video, Profile, Video
from .serializers import VideoSerializer, ProfileSerializer, ImageSerializer
from rest_framework.response import Response


class ProfileView(APIView):
    #Allow any user to hit this endpoint
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    # renderer_classes = (ProfileJSONRenderer,)

    def get(self, request, user_id, format=None):
        try:
            profile =  Profile.objects.get(user__id=user_id)
            serializer = ProfileSerializer(profile, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(
                {
                    'message': 'Profile not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, user_id, format=None):
        try:
            serializer_data = request.data.get('user', {})
            serializer = ProfileSerializer(
                request.user.profile,
                data=serializer_data,
                partial=True,
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(
                    {
                        'message': 'Profile not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )


