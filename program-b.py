import socket

def program_b():
    host = '127.0.0.1'  # This is the localhost IP
    port = 45000  # Port number used

    # Creating a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Binding the socket to the address and port
        server_socket.bind((host, port))

        # Listening on incoming connections
        server_socket.listen(1)
        print("Program B is listening for connections...")

        # Accepting the connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Receiving data from Program A
        data = conn.recv(1024).decode()
        print("Received from Program A:", data)

        # Converting response into uppercase
        response = data.upper()

        # Sending the response back
        conn.sendall(response.encode())

    except Exception as e:
        print("Error:", e)

    finally:
        # Close  connection
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    program_b()

