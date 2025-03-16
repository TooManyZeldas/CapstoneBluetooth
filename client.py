# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bluetooth

def client():

    bd_addr = "B8:27:EB:D0:60:19"

    port = 30

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    sock.send("Hello World!")

    sock.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
