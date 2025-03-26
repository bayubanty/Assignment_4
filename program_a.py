import socket

def program_a():
    host = '127.0.0.1'  # This is the localhost IP
    port = 45000  # Port number used

    # Creating a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connecting to Program_b
        client_socket.connect((host, port))

        # Getting the user input
        message = input("Enter a string to send: ")

        # Sending message
        client_socket.sendall(message.encode())

        # Receiving response from Program_b
        response = client_socket.recv(1024).decode()
        print("Received from Program_b:", response)

    except Exception as e:
        print("Error:", e)

    finally:
        # Closing socket
        client_socket.close()

if __name__ == "__main__":
    program_a()
