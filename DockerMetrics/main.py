import sys, time, json
from config import NODES_INI, api_url, timeout
from dock.nodes import Inventory
from dock.metrics import Metrics
import requests

# Add multiprocessing if possible when creating
# a request

if __name__ == '__main__':
    hosts   = Inventory(NODES_INI)
    print("Fetching Docker Metrics")
    print("Quit the server with CONTROL-C.")
    while True:
        try:
            docker_nodes   = hosts.get_inventory()
            for node in docker_nodes:
                if node == "localhost":
                    metric = Metrics("local")
                    container_ids   = metric.get_containerids()
                    for container_id in container_ids:
                        container_stats = metric.get_containerstats(container_id)
                        container_cpu   = metric.get_containercpu(container_stats)
                        container_mem   = metric.get_containermem(container_stats)
                else:
                    metric = Metrics("remote", node)
                    container_ids   = metric.get_containerids()
                    for container_id in container_ids:
                        container_stats = metric.get_containerstats(container_id)
                        container_cpu   = metric.get_containercpu(container_stats)
                        container_mem, container_usedmem, container_freemem   = metric.get_containermem(container_stats)
                        container_dict  = {
                            'node_ip'           : f"{node}",
                            'container_id'      : f"{container_id}",
                            'container_cpu'     : f"{container_cpu}",
                            'container_mem'     : f"{container_mem}",
                            'container_freemem' : f"{container_freemem}",
                            'container_usedmem' : f"{container_usedmem}"
                        }

                        container_json  = json.dumps(container_dict)
                        response        = requests.post(api_url, data=container_json)
                        print(response)


            time.sleep(timeout)
        except KeyboardInterrupt:
            print("[x] Closing...")
            sys.exit(0)

                    


        time.sleep(10)