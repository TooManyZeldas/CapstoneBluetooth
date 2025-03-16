# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bluetooth

# def connect_to_my_phone():
#     phone_address = "28:C5:38:9B:79:41"
#     port = 2
#     size = 1024
#     socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     socket.connect((phone_address, port))
#     try:
#         while 1:
#             data = socket.recv(size)
#             if data:
#                 print(data)
#     except:
#         print("closing socket")
#     socket.close()

def client():

    bd_addr = "B8:27:EB:D0:60:19"

    port = 1

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    sock.send("hello!!")

    sock.close()

# def server():
#     server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#
#     port = 1
#     server_sock.bind(("",port))
#     server_sock.listen(1)
#     print("Server Started. Listening on Port 1")
#
#     client_sock,address = server_sock.accept()
#     print("Accepted connection from ", address)
#
#     data = client_sock.recv(1024)
#     print("received [%s]" % data)
#
#     client_sock.close()
#     server_sock.close()





def find_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print(" {} - {}".format(addr, name))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_devices()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
