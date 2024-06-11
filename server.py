import socket
import threading
import os
from datetime import datetime

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 8080  # Choose any available port

# Directory to serve files from
BASE_DIR = 'www'

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected by {addr}")

    # Receive the HTTP request from the client
    request = conn.recv(1024).decode('utf-8')
    print("Request:")
    print(request)

    # Parse the HTTP request to get the requested file
    requested_file = request.split()[1]

    # If the file is '/', serve index.html
    if requested_file == '/':
        requested_file = '/index.html'

    # Construct the full file path
    file_path = os.path.join(BASE_DIR, requested_file[1:])

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the contents of the file
        with open(file_path, 'rb') as file:
            content = file.read()
        
        # Send HTTP response with the file content
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n".encode('utf-8') + content
    else:
        # File not found, send 404 error
        response = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found."

    # Send the HTTP response back to the client
    conn.sendall(response)

    # Log the request
    log_request(addr, requested_file, response)

    # Close the connection
    conn.close()

# Function to log the request
def log_request(addr, requested_file, response):
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_code = response.split()[1].decode('utf-8')
    log_entry = f"{addr[0]} - {access_time} - {requested_file} - {status_code}"

    with open('server_log.txt', 'a') as log_file:
        log_file.write(log_entry + '\n')

# Main function to start the server
def main():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))

        # Listen for incoming connections
        server_socket.listen()

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            # Accept incoming connection
            conn, addr = server_socket.accept()

            # Start a new thread to handle the client
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
