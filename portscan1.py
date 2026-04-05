import socket
from datetime import datetime

open_ports = []

def scan_ports(target, start_port, end_port):
    global open_ports
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scanning target: {target_ip}")
        
        start_time = datetime.now()

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)
            
            sock.close()

        end_time = datetime.now()
        print('\n' + '-' * 60)
        print(f'Open Ports Found: {len(open_ports)}')
        print(f'Open Ports: {open_ports}')
        print(f'Completed at: {end_time}')
        print(f'Duration: {end_time - start_time}')
        print('-' * 60)

    except socket.gaierror:
        print('Error: Hostname could not be resolved')

    except socket.error:
        print('Error: Could not connect to server')

    except KeyboardInterrupt:
        print('\nScan interrupted by user')

if __name__ == '__main__':
    target = input('Enter target host (IP/hostname): ')
    start_port = int(input('Enter start port: '))
    end_port = int(input('Enter end port: '))
    print()
    
    scan_ports(target, start_port, end_port)