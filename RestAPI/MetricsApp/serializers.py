from pyexpat import model
from rest_framework import serializers
from MetricsApp.models import DockerNodes, DockerMetrics

class DockerNodesSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DockerNodes
        fields  = (
            "node_id",
            "node_hostname",
            "node_ip"
            )

class DockerMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DockerMetrics
        fields  = (
            "metric_id",
            "node_ip",
            "node_hostname",
            "container_id",
            "container_cpu",
            "container_mem",
            "container_freemem",
            "container_usedmem",
            "container_ip",
            "datestamp",
            "timestamp"
            )