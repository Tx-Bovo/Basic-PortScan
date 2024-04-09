import socket
import threading
import argparse




# Um simples scan de portas
def scan_port(target, port, open_ports, lock):
    try:
        # Usa AF_INET para IPv4 e SOCK_STREAM para TCP/IP validando através do handshake SYN/ACK
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            
            with lock:
                open_ports.append(port)
                print(f"[+] {port} Open!")

    except (socket.timeout, ConnectionRefusedError):
        pass  # Porta fechada


# Threads para otimizar
def scan_ports_with_threads(target, init_port, end_port):
    open_ports = []
    lock = threading.Lock()
    threads = []

    for port in range(init_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return open_ports

def main():

    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('-t', '--target', required=True, help='Target')
    parser.add_argument('-a', '--all', action='store_true', help='For all ports')

    args = parser.parse_args()
    target = args.target
    all_ports = args.all
    # Scan de todas as portas TCP/IP
    if all_ports:
        init_port = 1
        end_port = 65535
    # Apenas as mais comuns
    else:
        init_port = 1
        end_port = 1024


    try:
        ports = scan_ports_with_threads(target, init_port, end_port)
    except Exception as e:
        # Tratamento de erros
        print(e)
        

if __name__ == '__main__':
    main()
