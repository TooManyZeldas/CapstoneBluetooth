# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bluetooth

def connect_to_my_phone():
    phone_address = "28:C5:38:9B:79:41"
    port = 2
    size = 1024
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((phone_address, port))
    try:
        while 1:
            data = socket.recv(size)
            if data:
                print(data)
    except:
        print("closing socket")
    socket.close()


# def broadcast():
#
#     # Set up the server socket using RFCOMM protocol
#     server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
#     # Bind the socket to any Bluetooth adapter and port 1
#     server_socket.bind(("", bluetooth.PORT_ANY))
#     server_socket.listen(1)
#
#     # Get the port number assigned to the socket
#     port = server_socket.getsockname()[1]
#
#     # Make the device discoverable
#     bluetooth.advertise_service(
#         server_socket,
#         "BluetoothServer",
#         service_id="00001101-0000-1000-8000-00805F9B34FB",
#         service_classes=["00001101-0000-1000-8000-00805F9B34FB", bluetooth.SERIAL_PORT_CLASS],
#         profiles=[bluetooth.SERIAL_PORT_PROFILE]
#     )
#
#     print(f"Waiting for connection on RFCOMM channel {port}...")
#
#     # Accept a connection
#     client_socket, client_info = server_socket.accept()
#     print(f"Accepted connection from {client_info}")
#
#     try:
#         while True:
#             # Receive data (maximum of 1024 bytes)
#             data = client_socket.recv(1024)
#             if not data:
#                 break
#             print(f"Received: {data.decode('utf-8')}")
#     except OSError:
#         pass
#
#     # Close the sockets
#     client_socket.close()
#     server_socket.close()




def find_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print(" {} - {}".format(addr, name))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_devices()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
