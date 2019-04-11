from django.urls import path
from .views import ProfileView, ImageView

urlpatterns = [
    path('<int:user_id>/', ProfileView.as_view(), name='user-profile'),
    path('<int:user_id>/image/', ImageView.as_view(), name='images'),
]