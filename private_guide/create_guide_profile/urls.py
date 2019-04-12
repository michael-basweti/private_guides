from django.urls import path
from .views import ImageView, VideoView, ImageDetail, VideoDetail

urlpatterns = [
    # path('<int:user_id>/', ProfileView.as_view(), name='user-profile'),
    path('<int:user_id>/image/', ImageView.as_view(), name='images'),
    path('<int:user_id>/image/<int:pk>', ImageDetail.as_view(), name='image_detail'),
    path('<int:user_id>/video/', VideoView.as_view(), name='videos'),
    path('<int:user_id>/video/<int:pk>', VideoDetail.as_view(), name='video_detail'),
]