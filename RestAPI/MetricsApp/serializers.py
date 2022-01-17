from pyexpat import model
from rest_framework import serializers
from MetricsApp.models import DockerMetrics

class DockerMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DockerMetrics
        fields  = (
            "metric_id",
            "node_ip",
            "container_id",
            "container_cpu",
            "container_mem",
            "container_freemem",
            "container_usedmem",
            "datestamp",
            "timestamp"
            )