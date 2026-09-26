import sys
import platform
import json
import socket

def get_os_info():
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "platform": platform.platform(),
        "architecture": platform.architecture(),
    }


def get_network_info():
    net_info = {}
    try:
        net_info["hostname"] = socket.gethostname()
        net_info["fqdn"] = socket.getfqdn()
        try:
            net_info["local_ip"] = socket.gethostbyname(socket.gethostname())
        except Exception:
            net_info["local_ip"] = "Не удалось определить"
    except Exception as e:
        net_info["error"] = str(e)
    return net_info


def get_python_info():
    return {
        "version": sys.version,
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "build": platform.python_build(),
    }

def main():
    data = {
        "os_info": get_os_info(),
        "network_info": get_network_info(),
        "python_info": get_python_info(),
    }

    filename = "system_info.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Информация сохранена в файл: {filename}")

if __name__ == "__main__":
    main()