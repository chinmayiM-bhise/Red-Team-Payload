import platform
import psutil
import socket
import requests

SERVER = "http://localhost:5000"

def collect_system_info():

    return {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "os_version": platform.version(),
        "cpu": platform.processor(),
        "ram_gb": round(psutil.virtual_memory().total / (1024**3),2),
        "process_count": len(psutil.pids())
    }


def register():

    data = collect_system_info()

    r = requests.post(SERVER + "/register", json=data)

    print("Registered:", r.json())


if __name__ == "__main__":
    register()