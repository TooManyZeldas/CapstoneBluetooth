import bluetooth

def client():

    bd_addr = "B8:27:EB:D0:60:19"

    port = 30

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    sock.send("Hello World!")

    sock.close()

if __name__ == '__main__':
    client()