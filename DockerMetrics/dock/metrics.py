import docker

class Metrics:
    def __init__(self, state, node=None):
        self.state                          = state

        if self.state == "remote":
            self.node   = node
            self.client = docker.DockerClient(base_url=f"tcp://{self.node}:2375")
        else:
            self.client = docker.from_env()

    def get_containerids(self):
        return self.client.containers.list()

    def get_containerstats(self, container_id):
        return container_id.stats(decode=None, stream=False)

    def get_containercpu(self, container_stats):
        cpu_count       = len(container_stats["cpu_stats"]["cpu_usage"]["percpu_usage"])
        cpu_delta       = container_stats['cpu_stats']['cpu_usage']['total_usage'] - container_stats['precpu_stats']['cpu_usage']['total_usage']
        system_delta    = container_stats['cpu_stats']['system_cpu_usage'] - container_stats['precpu_stats']['system_cpu_usage']
        cpu_percent     = (cpu_delta / system_delta) * cpu_count * 100
        return round(cpu_percent)
        
    def get_containermem(self, container_stats):
        container_mem       = container_stats['memory_stats']['limit']
        container_usedmem   = container_stats['memory_stats']['usage']
        container_freemem   = container_mem - container_usedmem
        return round(container_mem /1024.0**2), round(container_usedmem /1024.0**2), round(container_freemem /1024.0**2)