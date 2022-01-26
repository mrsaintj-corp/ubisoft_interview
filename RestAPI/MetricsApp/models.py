from django.db import models

# Create your models here.
class DockerMetrics(models.Model):
    metric_id           = models.AutoField(primary_key=True)
    node_ip             = models.CharField(max_length=50)
    container_id        = models.CharField(max_length=50)
    container_cpu       = models.IntegerField()
    container_mem       = models.IntegerField()
    container_freemem   = models.IntegerField()
    container_usedmem   = models.IntegerField()
    created_on          = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class DockerNodes(models.Model):
    node_id = models.AutoField(primary_key=True)
    node_ip = models.CharField(max_length=50)