from django.urls import path
from .views import ImageView, VideoView, ImageDetail, VideoDetail

urlpatterns = [
    # path('<int:user_id>/', ProfileView.as_view(), name='user-profile'),
    path('image/', ImageView.as_view(), name='images'),
    path('image/<int:pk>', ImageDetail.as_view(), name='image_detail'),
    path('video/', VideoView.as_view(), name='videos'),
    path('video/<int:pk>', VideoDetail.as_view(), name='video_detail'),
]