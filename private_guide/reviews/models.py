from django.db import models
from authentication.models import User
from create_guide_profile.models import Profile


class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name="reviewer", on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, related_name="profile_id", on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
