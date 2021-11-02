import uuid
from django.db import models

class User(models.Model):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=150)

  def __str__(self):
    return self.name
