import os
from socket import timeout

ROOT_DIR    = os.path.dirname(os.path.abspath(__file__))
NODES_INI   = os.path.join(ROOT_DIR, 'nodes.ini')

api_url     = "http://127.0.0.1:8000/metric"
timeout     = 10