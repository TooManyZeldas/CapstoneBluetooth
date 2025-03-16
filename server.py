# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bluetooth

def server():
    server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    port = 30

    server_sock.bind(("",port))
    server_sock.listen(1)
    print(f"Server Started. Listening on port {port}")
    client_sock,address = server_sock.accept()
    print("Accepted connection from ", address)

    data = client_sock.recv(1024)
    print("received [%s]" % data)

    client_sock.close()
    server_sock.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
