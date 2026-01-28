import json
import arg_parser
import port_scanner


config_file_name = "config.json"
version_val = 0.1
parser = arg_parser.parse_args()
arg_parser.save_config(parser, config_file_name)


with open(config_file_name, "r") as f:
    config_dict = json.load(f)

host = config_dict["host"]
ports = config_dict["port"]
proto = config_dict["proto"]
timeout = config_dict["timeout"]
verbose = config_dict["verbose"]
version = config_dict["version"]

open_ports = []

if version:
    print(f"Version: {version_val}")
    exit()

port_scanner.resolve_host(host, proto)

print(f"Scanning ports {ports[0]} - {ports[-1]} for host: {host} ...")

for port in ports:
    if port_scanner.scan_port(port, timeout):
        open_ports.append(port)

if len(open_ports) > 0:
    print(f"Open ports: {open_ports}")
else:
    print("No open ports found")


# To clear the json file
with open('data.json', 'w') as f:
        pass


