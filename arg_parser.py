import json
import argparse


# parser argument is only used for parser.error
def parse_ports(port_args, parser):
    range_count = 0
    ports = set()
    for part in port_args:
        if "-" in part:
            range_count += 1
            if range_count > 1:
                parser.error("Only one range allowed")
            start, end = part.split("-", 1)
            start, end = int(start), int(end)
            if not (1 <= start <= 65535 and 1 <= end <= 65535):
                parser.error("Port numbers must be in 1-65535")
            if end < start:
                parser.error("Invalid port range: start must be <= end")
            else:
                ports.update(range(start, end + 1))
        else:
            port = int(part)
            if not (1 <= port <= 65535):
                parser.error("Port numbers must be in 1-65535")
            else:
                ports.add(port)
    return sorted(ports)





def parse_args():
    parser = argparse.ArgumentParser(description="Port Scanner")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-H", "--host", type=str, help="Target IP(IPv4/IPv6) or domain")

    group.add_argument("-v", "--version", action="store_true", help="Show version")

    parser.add_argument("-p", "--port", nargs="+", type=str, required=True, help="port(s) to scan, a single number or multiple numbers(seprated by space) or a range(x-y)")

    parser.add_argument("-P", "--proto", choices=["tcp", "udp"], default="tcp", help="Protocol(tcp/udp)")

    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Max timeout in sec(float)")

    parser.add_argument("-V", "--verbose", action="store_true", help="Active verbose mode")
 
    return parser




def save_config(parser, config_file_name):
    args = parser.parse_args()

    config_dict = vars(args)
    ports = parse_ports(config_dict["port"], parser)
    config_dict["port"] = ports
    with open(config_file_name, "w") as f:
        json.dump(config_dict, f, indent=4)




