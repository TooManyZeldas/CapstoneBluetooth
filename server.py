import bluetooth
import json

def server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 30
    server_sock.bind(("", port))
    server_sock.listen(1)

    print(f"Server Started. Listening on port {port}")
    client_sock, address = server_sock.accept()
    print("Accepted connection from", address)

    data = b"" #intialize empty bytes object

    while True:
        try:
            chunk = client_sock.recv(1024) #read in chunks of 1024 bytes
            if not chunk: #if no data is received, break loop
                break
            data += chunk #append bytes received

            if b"<EOF>" in data: #stop when end of file marker is found
                data = data.replace(b"<EOF>", b"") #remove the end of file marker
                break
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")
            break

    json_str = data.decode("utf-8") #decode bytes received
    try:
        json_data = json.loads(json_str) #parse json
        print("Received JSON:", json_data)
    except json.JSONDecodeError:
        print("Error decoding JSON")

    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    server()

