from platform import node
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MetricsApp.models import DockerNodes, DockerMetrics
from MetricsApp.serializers import DockerNodesSerializer, DockerMetricsSerializer

# Create your views here.
@csrf_exempt
def dockernodeApi(request, id=0):
    if request.method == 'GET':
        nodes               = DockerNodes.objects.all()
        nodes_serializer    = DockerNodesSerializer(nodes, many=True)
        return JsonResponse(nodes_serializer.data, safe=False)
    elif request.method == 'POST':
        node_data           = JSONParser().parse(request)
        nodes_serializer    = DockerNodesSerializer(data=node_data)
        if nodes_serializer.is_valid():
            nodes_serializer.save()
            return JsonResponse("Successfully Added the Entry", safe=False)
        return JsonResponse("Failed to Add the Entry")
    elif request.method == 'PUT':
        node_data           = JSONParser().parse(request)
        node_id             = DockerNodes.objects.get(node_id=node_data['node_id'])
        nodes_serializer    = DockerNodesSerializer(node_id, data=node_data)
        if nodes_serializer.is_valid():
            nodes_serializer.save()
            return JsonResponse("Updated the Entry", safe=False)
        return JsonResponse("Failed to Update Entry")
    elif request.method == 'DELETE':
        node    = DockerNodes.objects.get(node_id=id)
        node.delete()
        return JsonResponse("Successfully Deleted the Entry", safe=False)
        
@csrf_exempt
def dockermetricsApi(request, id=0):
    if request.method == 'GET':
        metric              = DockerMetrics.objects.all()
        metric_serializer   = DockerMetricsSerializer(metric, many=True)
        return JsonResponse(metric_serializer.data, safe=False)
    elif request.method == 'POST':
        metric_data         = JSONParser().parse(request)
        metrics_serializer  = DockerMetricsSerializer(data=metric_data)
        if metrics_serializer.is_valid():
            metrics_serializer.save()
            return JsonResponse("Successfully Added the Entry", safe=False)
        return JsonResponse("Failed to Add the Entry")
    elif request.method == 'PUT':
        metric_data         = JSONParser().parse(request)
        metric_id           = DockerMetrics.objects.get(metric_id=metric_data['metric_id'])
        metric_serializer   = DockerMetricsSerializer(metric_id, data=metric_data)
        if metric_serializer.is_valid():
            metric_serializer.save()
            return JsonResponse("Updated the Entry", safe=False)
        return JsonResponse("Failed to Update Entry")
    elif request.method == 'DELETE':
        metric    = DockerMetrics.objects.get(metric_id=id)
        metric.delete()
        return JsonResponse("Successfully Deleted the Entry", safe=False)