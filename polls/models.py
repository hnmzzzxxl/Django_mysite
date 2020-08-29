import uuid

from django.db import models


class Batch(models.Model):
    class Meta:
        db_table = 'batch'
        ordering = ['t_count']

    create_timestamp = models.IntegerField(null=True)
    create_datetime = models.DateTimeField()
    t_count = models.IntegerField(default=False)
    b_uuid = models.UUIDField(default=uuid.uuid4())
