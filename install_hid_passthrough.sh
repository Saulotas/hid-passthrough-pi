#!/bin/bash

set -e

echo "🔧 Installing HID Passthrough System..."

# Update system
sudo apt update
sudo apt install -y python3 python3-pip python3-hid python3-dbus bluetooth bluez

# Enable Bluetooth
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

# Create install directory
sudo mkdir -p /opt/hid-passthrough
sudo cp -r src /opt/hid-passthrough/
sudo cp config.yaml /opt/hid-passthrough/

# Install Python requirements
sudo pip3 install pybluez hid python-systemd PyYAML

# Setup udev rules for hidraw access
sudo cp udev/99-hidraw.rules /etc/udev/rules.d/
sudo udevadm control --reload
sudo udevadm trigger

# Install systemd services
sudo cp systemd/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable hid_passthrough.service
sudo systemctl enable bt_autopair.service
sudo systemctl enable bt_led_status.service

echo "✅ Installation complete!"
echo "💡 Please reboot your Pi now."
