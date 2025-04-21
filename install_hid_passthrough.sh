#!/bin/bash
# install_hid_passthrough.sh - Installer for HID Passthrough Pi
# Author: Saulotas

set -e

echo "🛠️ HID Passthrough Pi Installer Started..."

# --- Update apt and install required system packages ---
echo "📦 Installing system packages..."
sudo apt update
sudo apt install -y python3-pip python3-hid python3-dbus bluetooth bluez build-essential libbluetooth-dev git

# --- Fix PyBluez if needed ---
echo "🔧 Checking and fixing PyBluez installation if needed..."
bash /opt/hid-passthrough-pi/scripts/fix_pybluez.sh

# --- Install required Python packages ---
echo "📦 Installing Python libraries..."
pip install --break-system-packages pyyaml

# --- Create and install systemd services ---
echo "🔧 Installing systemd services..."

SERVICE_PATH="/etc/systemd/system"

# HID Passthrough Service
sudo cp /opt/hid-passthrough-pi/services/hid_passthrough.service $SERVICE_PATH/
sudo systemctl enable hid_passthrough.service

# Bluetooth Auto Pair Service
sudo cp /opt/hid-passthrough-pi/services/bt_auto_pair.service $SERVICE_PATH/
sudo systemctl enable bt_auto_pair.service

# Bluetooth LED Status Service
sudo cp /opt/hid-passthrough-pi/services/bt_led_status.service $SERVICE_PATH/
sudo systemctl enable bt_led_status.service

# OTA Updater Service
sudo cp /opt/hid-passthrough-pi/services/ota_updater.service $SERVICE_PATH/
sudo systemctl enable ota_updater.service

echo "✅ Services installed and enabled."

# --- Setup directories if needed ---
echo "📁 Ensuring necessary folders exist..."
mkdir -p /opt/hid-passthrough-pi/logs

# --- Final steps ---
echo "🚀 Installation complete!"
echo "➡️ Reboot your Pi to start services:"
echo "   sudo reboot"

exit 0
