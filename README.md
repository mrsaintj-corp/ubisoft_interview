# DockerMetricsAPI

This project uses Django Rest Framework and Docker SDK to pull Docker stats locally or remotely.

## Installation
 I've included a requirements file that can easily install the necessary packages. It will be located at the root of the directory.

`pip install -r requirements.txt`

## Database
 There are currently two tables in the SQLite database which are located in the RestAPI folder. The MetricsApp_dockermetrics table is used to store information such as the metric_id, node_ip, container_id, container_cpu, container_mem, container_freemem, container_usedmem, datestamp and timestamp. While the MetricsApp_dockernodes is used to store the node_id and the node_ip. The MetricsApp_dockernodes table isn't currently used in the project. I was planning to use it to get live updates from each node. Unfortunately, I didn't have the time this week to implement that portion of the code. I've included some data I ran locally inside the database to test with.

**MetricsApp_dockermetrics**
| metric_id | node_ip | container_id | container_cpu | container_mem | container_freemem | container_usedmem | datestamp | timestamp |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| AutoField | CharField | CharField | IntegerField | IntegerField | IntegerField | IntegerField | DateField | TimeField |

**MetricsApp_dockernodes**
| node_id | node_ip |
| ------ | ------ |
| AutoField | CharField |

## Docker Stats
 In order to grab the Docker stats, I used the [Docker SDK.](https://docker-py.readthedocs.io/en/stable/) This allowed me to use the Docker Engine API locally or remotely. Inside of the DockerMetrics folder, there is a inventory file called nodes.ini which can either take a IP or a hostname. If you'd like to run it locally, all you need to specify is localhost inside the nodes.ini file.(localhost is the default host) Before running this portion of the script, you must ensure that the Django server is running first, as the script expects the server to be reachable.

 To start grabbing Docker stats, run the main.py file inside of the DockerMetrics folder.

`python main.py`

## Django REST Framework
 I decided to use [Django REST Framework](https://www.django-rest-framework.org/) to build my API. 
 
 To start the Django server, you have to run the following command in the RestAPI directory.

 `python manage.py runserver`

 These are the GET methods I've created

 **Grab all metrics**

 `http://127.0.0.1:8000/metric/api/`

 **Grab a specific metric**

`http://127.0.0.1:8000/metric/api/1`

**Grab a metric by the container_id**

`http://127.0.0.1:8000/metric/api/containers?container_id=da49480343`

**Grab a metric by the node_ip**

`http://127.0.0.1:8000/metric/api/nodes?node_ip=10.29.42.12`

**Grab the last N records**

`http://127.0.0.1:8000/metric/api/records?last=22`

**Grab CPU percentages that are greater than or equal to**

`http://127.0.0.1:8000/metric/api/cpu?cpu_gte=70`

**Grab CPU percentages that are less than or equal to**

`http://127.0.0.1:8000/metric/api/cpu?cpu_lte=70`

**Grab free memory that is greater than or equal to**

`http://127.0.0.1:8000/metric/api/mem?mem_gte=7355`

**Grab free memory that is less than or equal to**

`http://127.0.0.1:8000/metric/api/mem?mem_lte=7253`

**Grab date that is after X**

`http://127.0.0.1:8000/metric/api/date?date_after=2022-01-20`

**Grab date that is before X**

`http://127.0.0.1:8000/metric/api/date?date_before=2022-01-19`
