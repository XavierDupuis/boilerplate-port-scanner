import socket
import common_ports
import sys

def print_descrpitive(open_ports, target):
    output = ""
    output += "Open ports for " + target
    if target != socket.gethostbyname(target):
         output += " (" + socket.gethostbyname(target) + ")" + "\n"
    else:
         output += "\n"
    output += "PORT\tSERVICE\n"
    for port in open_ports:
        output += str(port) + "\t" + common_ports.ports_and_services[port] + "\n"
    return output

def test_port(host, port):
    s = socket.socket()
    isPortOpen = True
    try:
        s.settimeout(0.2)
        s.connect((host, port))
    except:
        isPortOpen = False
    finally:
        s.close()
        return isPortOpen

def test_IP(target):
    test = True
    try:
        socket.inet_aton(socket.gethostbyname(target))
    except:
        test = False
    return test

def test_URL(target):
    test = True
    try:
        socket.gethostbyname(target)
    except:
        test = False
    return test

# https://stackoverflow.com/questions/30626182/determine-if-host-is-domain-name-or-ip-in-python
def is_ip(address):
    return not address.split('.')[-1].isalpha()

def get_open_ports(target, port_range, verbose=False):
    if is_ip(target):
        if not test_IP(target):
            return "Error: Invalid IP address"
    else:
        if not test_URL(target):
            return "Error: Invalid hostname"

    open_ports = []
    for port in range(port_range[0], port_range[1]+1):
        if(test_port(target, port)):
            open_ports.append(port)

    if verbose:
        open_ports = print_descrpitive(open_ports, target)

    return(open_ports)

def get_open_common_ports(target, verbose=False):
    if is_ip(target):
        if not test_IP(target):
            return "Error: Invalid IP address"
    else:
        if not test_URL(target):
            return "Error: Invalid hostname"

    open_ports = []
    for port in common_ports.ports_and_services:
        if(test_port(target, port)):
            open_ports.append(port)

    if verbose:
        open_ports = print_descrpitive(open_ports, target)

    return(open_ports)

if __name__ == "__main__":
    try:
        print(get_open_ports(sys.argv[1], [int(sys.argv[2]), int(sys.argv[3])], sys.argv[4]))
    except:
        try:
            print(get_open_ports(sys.argv[1], [int(sys.argv[2]), int(sys.argv[3])]))
        except:
            print(get_open_common_ports(sys.argv[1], True))
