from django.db import models
from rapidsms.models import Connection


class ContactState(models.Model):
    connection = models.ForeignKey(Connection)
    handler = models.CharField(max_length=256)