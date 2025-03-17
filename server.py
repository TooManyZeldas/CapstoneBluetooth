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

    data = b""

    while True:
        try:
            chunk = client_sock.recv(1024)
            if not chunk:
                break
            data += chunk

            if b"<EOF>" in data:
                data = data.replace(b"<EOF>", b"")
                break
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth error: {e}")
            break

    json_str = data.decode("utf-8")
    try:
        json_data = json.loads(json_str)
        print("Received JSON:", json_data)

        response_msg = json.dumps({"status": "Received successfully"})
        client_sock.send(response_msg.encode("utf-8"))

    except json.JSONDecodeError:
        print("Error decoding JSON")
        client_sock.send(json.dumps({"status": "Error decoding JSON"}).encode("utf-8"))

    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    server()