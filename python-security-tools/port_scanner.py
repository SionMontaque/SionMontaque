# basic TCP port scanner
import socket

def scan(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            s.close()

if __name__ == '__main__':
    target = input("Enter target IP or hostname: ")
    ports = [21,22,23,25,53,80,110,143,443,3306]
    scan(target, ports)
