# HID Passthrough Pi

This project allows you to use a **Raspberry Pi Zero W** (or similar Raspberry Pi) as a **USB HID passthrough device**. The Pi acts as a bridge to forward keyboard input (wired USB) to a **Bluetooth-connected** device. This setup allows for seamless keyboard connectivity between a **USB keyboard** and a **Bluetooth-enabled PC** or **smartphone**.

## 🛠️ Features:
- **USB HID passthrough**: Wired keyboard to Bluetooth device.
- **Automatic pairing**: The Pi will automatically pair with a Bluetooth device.
- **LED status**: Visual indication of Bluetooth connection using an LED.
- **Over-the-Air (OTA) updates**: Keep your Pi up-to-date automatically.

---

## ⚙️ Hardware Setup:

1. **Pi Zero W** (or other compatible Raspberry Pi with Bluetooth).
2. **USB keyboard**: Plug it into the Pi's USB OTG port (you'll need a USB OTG adapter).
3. **LED** (optional): Connect an LED to a GPIO pin on the Pi (to show connection status).
   - **GPIO Pin**: Configure in `config.yaml` (default is disabled, set `led_pin: -1` to turn off).

---

## 📋 Software Setup:

### 1. Install Dependencies:
Run the provided installation script to set up everything automatically:

```bash
bash install_hid_passthrough.sh
