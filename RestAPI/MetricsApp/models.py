from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class DockerNodes(models.Model):
    node_id         = models.AutoField(primary_key=True)
    node_hostname   = models.CharField(max_length=120)
    node_ip         = models.CharField(max_length=50)

class DockerMetrics(models.Model):
    metric_id           = models.AutoField(primary_key=True)
    node_ip             = models.CharField(max_length=50)
    node_hostname       = models.CharField(max_length=120)
    container_id        = models.CharField(max_length=18)
    container_cpu       = models.CharField(max_length=10)
    container_mem       = models.CharField(max_length=30)
    container_freemem   = models.CharField(max_length=20)
    container_usedmem   = models.CharField(max_length=20)
    container_ip        = models.CharField(max_length=200)
    datestamp           = models.DateField(auto_now_add=True, blank=True)
    timestamp           = models.TimeField(auto_now_add=True, blank=True)