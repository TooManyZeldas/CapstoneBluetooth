# CAPSTONE

## If no (.venv) prefix:

source .venv/bin/activate

## If no bluetooth module:

python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

## Check if bluetooth is working:

sudo systemctl status bluetooth

## If no bluetooth on PI:

sudo apt update

sudo apt install --reinstall bluez

sudo systemctl restart bluetooth

## To manually pair with device

bluetoothctl

scan

trust “xx:xx:xx:xx:xx:xx”