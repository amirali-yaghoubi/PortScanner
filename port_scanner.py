import socket


_addrinfos = None

def resolve_host(host : str, socket_type : str):
    global _addrinfos
        
    if _addrinfos == None:
        if socket_type.lower() == "tcp":
            sock_type = socket.SOCK_STREAM
        elif socket_type.lower() == "udp":
            sock_type = socket.SOCK_DGRAM
        else:
            raise ValueError("Unsupported protocol.")

        _addrinfos = socket.getaddrinfo(host, None, 0, sock_type)



def scan_port(port : int, timeout : float) -> bool:
    for family, socktype, proto, canonname, sockaddr in _addrinfos:
        try:
            with socket.socket(family, socktype, 0) as s:
                s.settimeout(timeout)
                host = sockaddr[0]
                s.connect((host, port))
                return True
        except Exception:
            continue
    return False










