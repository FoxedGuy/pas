import socket
from time import sleep

# generate permutations of the given list
def generate_permutation_of_ports(ports):
    permutations = []
    for i in range(0, len(ports)):
        for j in range(0, len(ports)):
            for k in range(0, len(ports)):
                if i != j and j != k and i != k:
                    permutations.append([ports[i], ports[j], ports[k]])
    return permutations

def main():
    # udp_ports = []
    # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sockUDP:
    #     for i in range (0,65):
    #         try:
    #             sockUDP.connect(("localhost", i*1000+666))
    #             sockUDP.send("PING".encode('utf-8'))
    #             response = sockUDP.recv(1024)
    #             if response.decode('utf-8') == "PONG":
    #                 udp_ports.append(i*1000+666)
    #                 print("UDP port found: {}".format(i*1000+666))
    #         except Exception:
    #             print("UDP port not found: {}".format(i*1000+666))
    #     print(udp_ports)
    #     permutations = generate_permutation_of_ports(udp_ports)
    #     print(permutations)
    #
    # sockUDP.close()
    ports = [17666, 34666, 53666]
    # try knocking on each port permutation
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sockUDP2:
        permutations = generate_permutation_of_ports(ports)
        for permutation in permutations:
            for port in ports:
                sockUDP2.connect(("localhost", port))
                sockUDP2.send("PING".encode('utf-8'))
                sleep(3)


if __name__ == '__main__':
    main()