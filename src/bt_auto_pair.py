#!/usr/bin/env python3
import os
import time
import subprocess
import yaml

# Load configuration
with open('/opt/hid-passthrough/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

PAIRING_MODE = config.get('bt_pairing_mode', 'auto')

def make_discoverable():
    os.system("bluetoothctl discoverable on")
    os.system("bluetoothctl pairable on")
    os.system("bluetoothctl agent NoInputNoOutput")
    os.system("bluetoothctl default-agent")

def auto_pair_loop():
    while True:
        try:
            output = subprocess.check_output("bluetoothctl paired-devices", shell=True).decode()
            if not output.strip():
                print("[BT AutoPair] No paired devices. Setting discoverable mode...")
                make_discoverable()
            else:
                print("[BT AutoPair] Already paired device found.")
            time.sleep(10)
        except Exception as e:
            print(f"[BT AutoPair] Error: {e}")
            time.sleep(5)

def main():
    if PAIRING_MODE == "auto":
        auto_pair_loop()
    else:
        print("[BT AutoPair] Manual mode selected, exiting.")

if __name__ == "__main__":
    main()
