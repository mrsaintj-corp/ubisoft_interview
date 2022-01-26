from django_filters import FilterSet, DateTimeFilter, NumberFilter 
from MetricsApp.models import DockerMetrics

class MetricCpuFilter(FilterSet):
    cpu_lte = NumberFilter(field_name="container_cpu", lookup_expr='lte')
    cpu_gte = NumberFilter(field_name="container_cpu", lookup_expr='gte')

    class Meta:
        model   = DockerMetrics
        fields  = ['container_cpu']

class MetricFreeMemFilter(FilterSet):
    mem_lte = NumberFilter(field_name="container_freemem", lookup_expr='lte')
    mem_gte = NumberFilter(field_name="container_freemem", lookup_expr='gte')

    class Meta:
        model   = DockerMetrics
        fields  = ['container_freemem']

class MetricDateFilter(FilterSet):
    date_before = DateTimeFilter(field_name="created_on", lookup_expr='lte')
    date_after  = DateTimeFilter(field_name="created_on", lookup_expr='gte')

    class Meta:
        model   = DockerMetrics
        fields  = ['created_on']