import sys, time, json
from config import NODES_INI, api_url, timeout, DB_PATH
from dock.nodes import Inventory
from dock.metrics import Metrics
from database.database import Database

if __name__ == '__main__':
    hosts   = Inventory(NODES_INI)
    print("Fetching Docker Metrics")
    print("Quit the server with CONTROL-C.")
    while True:
        try:
            docker_nodes        = hosts.get_inventory()
            dockermetrics_db    = Database(DB_PATH, "MetricApp_dockermetrics")
            for node in docker_nodes:
                if node == "localhost":
                    metric = Metrics("local")
                else:
                    metric = Metrics("remote", node)
                container_ids   = metric.get_containerids()
                for container_id in container_ids:
                    container_stats = metric.get_containerstats(container_id)
                    container_cpu   = metric.get_containercpu(container_stats)
                    container_mem, container_usedmem, container_freemem   = metric.get_containermem(container_stats)
                    container_id    = f"{container_id}".split()[1].split(">")[0]

                    container_dict  = {
                        'node_ip'           : f"{node}",
                        'container_id'      : f"{container_id}",
                        'container_cpu'     : container_cpu,
                        'container_mem'     : container_mem,
                        'container_freemem' : container_freemem,
                        'container_usedmem' : container_usedmem
                    }
                    dockermetrics_db.create_entry(container_dict)

            dockermetrics_db.close_session()
            time.sleep(timeout)
        except KeyboardInterrupt:
            print("[x] Closing...")
            sys.exit(0)