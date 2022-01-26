from rest_framework import serializers
from MetricsApp.models import DockerMetrics, DockerNodes

class DockerMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DockerMetrics
        fields  = '__all__'

class DockerNodesSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DockerMetrics
        fields  = '__all__'