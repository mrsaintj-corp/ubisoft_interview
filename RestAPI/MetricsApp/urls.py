from django.urls import path
from MetricsApp.views import MetricList, MetricDetailId, MetricDetailContainerId, MetricDetailNode, MetricDetailLastNRecords, MetricDetailCpu, MetricDetailFreeMem, MetricDetailDateTime, MetricLive

urlpatterns = [
    # http://127.0.0.1:8000/metric/api/
    path('api/', MetricList.as_view(), name='listcreate'),
    # http://127.0.0.1:8000/metric/api/2
    path('api/<int:pk>', MetricDetailId.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/containers?container_id=f38239ded5
    path('api/containers', MetricDetailContainerId.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/nodes?node_ip=10.29.42.12
    path('api/nodes', MetricDetailNode.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/records?last=22
    path('api/records', MetricDetailLastNRecords.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/cpu?cpu_gte=70
    # http://127.0.0.1:8000/metric/api/cpu?cpu_lte=70
    path('api/cpu', MetricDetailCpu.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/mem?mem_gte=7255
    # http://127.0.0.1:8000/metric/api/mem?mem_lte=7255
    path('api/mem', MetricDetailFreeMem.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/date?date_after=2022-01-20
    # http://127.0.0.1:8000/metric/api/date?date_before=2022-01-19
    path('api/date', MetricDetailDateTime.as_view(), name='detailcreate'),
    # http://127.0.0.1:8000/metric/api/live
    path('api/live', MetricLive.as_view(), name='detailcreate'),
]