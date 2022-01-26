from rest_framework import generics

from MetricsApp.models import DockerMetrics, DockerNodes
from MetricsApp.serializers import DockerMetricsSerializer
from MetricsApp.filters import MetricCpuFilter, MetricFreeMemFilter, MetricDateFilter

# Create your views here.
class MetricList(generics.ListCreateAPIView):
    serializer_class = DockerMetricsSerializer

    def get_queryset(self, *args, **kwargs):
        schemes = DockerMetrics.objects.all()
        return schemes

class MetricDetailId(generics.RetrieveAPIView):
    queryset            = DockerMetrics.objects.all()
    serializer_class    = DockerMetricsSerializer

    def get_queryset(self):
        metric_id   = self.kwargs['pk']
        return DockerMetrics.objects.filter(metric_id=metric_id)
    
class MetricDetailContainerId(generics.ListAPIView):
    serializer_class    = DockerMetricsSerializer

    def get_queryset(self):
        container_id   = self.request.query_params.get('container_id', None)
        return DockerMetrics.objects.filter(container_id=container_id)
    
class MetricDetailNode(generics.ListAPIView):
    serializer_class    = DockerMetricsSerializer

    def get_queryset(self):
        node   = self.request.query_params.get('node_ip', None)
        return DockerMetrics.objects.filter(node_ip=node)

class MetricDetailLastNRecords(generics.ListAPIView):
    serializer_class    = DockerMetricsSerializer

    def get_queryset(self):
        last_n      = self.request.query_params.get('last', 10)
        api_data    = DockerMetrics.objects.all().order_by('-metric_id')[:int(last_n)]
        return reversed(api_data)

class MetricDetailCpu(generics.ListAPIView):
    queryset            = DockerMetrics.objects.all()
    serializer_class    = DockerMetricsSerializer
    filterset_fields    = ('container_cpu')
    filterset_class     = MetricCpuFilter

class MetricDetailFreeMem(generics.ListAPIView):
    queryset            = DockerMetrics.objects.all()
    serializer_class    = DockerMetricsSerializer
    filterset_fields    = ('container_freemem')
    filterset_class     = MetricFreeMemFilter

class MetricDetailDateTime(generics.ListAPIView):
    queryset            = DockerMetrics.objects.all()
    serializer_class    = DockerMetricsSerializer
    filterset_fields    = ('created_on')
    filterset_class     = MetricDateFilter

class MetricLive(generics.ListAPIView):
    serializer_class    = DockerMetricsSerializer

    def get_queryset(self):
        scheme   = DockerMetrics.objects.filter()
        return scheme