from django.db import models
from authentication.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=False, blank = False)
    body = models.TextField(null=False, blank = False)
    image = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
