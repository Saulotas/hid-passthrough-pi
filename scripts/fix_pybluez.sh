#!/bin/bash
# fix_pybluez.sh - Fixes PyBluez installation on Raspberry Pi OS Bookworm (Python 3.11+)

set -e

echo "🔧 Installing build-essential and libbluetooth-dev..."
sudo apt update
sudo apt install -y build-essential libbluetooth-dev git

echo "🔧 Cloning the updated pybluez repository..."
cd /opt
if [ ! -d "pybluez" ]; then
    sudo git clone https://github.com/pybluez/pybluez.git
else
    cd pybluez
    sudo git pull
fi

echo "🔧 Installing pybluez from source..."
cd /opt/pybluez
sudo python3 setup.py install

echo "✅ PyBluez installed successfully!"
