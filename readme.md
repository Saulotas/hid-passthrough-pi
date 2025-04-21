# HID Passthrough Pi

Make a Raspberry Pi Zero W (or Pi Zero 2 W) act as a **Bluetooth keyboard/mouse adapter** for any wired USB keyboard (QMK or standard).

---

## 📦 Features

- USB host to Bluetooth HID passthrough
- Full support for QMK keyboards, including media keys
- Built-in auto-pairing system
- LED status indicator (pairing / connected)
- OTA (Over-the-Air) Updater support
- Clean install/uninstall
- PyBluez fixes included for Pi OS Bookworm (Python 3.11+)

---

## 🚀 Quick Install

Clone the repo:

```bash
cd /opt
sudo git clone https://github.com/Saulotas/hid-passthrough-pi.git
cd hid-passthrough-pi
sudo bash install_hid_passthrough.sh
