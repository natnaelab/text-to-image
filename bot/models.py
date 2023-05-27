from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class User(BaseModel):
    tid = models.CharField(max_length=50)
    is_banned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    message_count = models.PositiveIntegerField(default=1)
    last_message_at = models.DateTimeField(default=timezone.now)
