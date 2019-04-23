"""private_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from create_guide_profile.views import ProfileViewSet, ReviewViewSet, UserProfile
from blog.views import BlogViewSet, CommentViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('reviews', ReviewViewSet)
router.register('blog', BlogViewSet)
router.register('comments', CommentViewSet)
router.register('myProfile', UserProfile, base_name='UserProfile',)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('authentication/',include(('authentication.urls','authentication'), namespace='authentication')),
    path('profile_files/',include(('create_guide_profile.urls','profile_files'), namespace='profile_files')),
]
