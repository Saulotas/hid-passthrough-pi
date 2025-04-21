#!/usr/bin/env python3
import os
import time
import threading
import hid
import dbus
import yaml

# Load configuration
with open('/opt/hid-passthrough/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

DEVICE_NAME = config.get('device_name', 'HIDPassthroughPi')
HID_POLL_INTERVAL = config.get('hid_poll_interval', 0.003)

# Bluetooth HID Setup
class BluetoothHID:
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.adapter = self._get_adapter()

    def _get_adapter(self):
        manager = dbus.Interface(
            self.bus.get_object('org.bluez', '/'),
            'org.freedesktop.DBus.ObjectManager'
        )
        objects = manager.GetManagedObjects()
        for path, interfaces in objects.items():
            if 'org.bluez.Adapter1' in interfaces:
                return self.bus.get_object('org.bluez', path)
        raise Exception("Bluetooth adapter not found")

    def setup_device(self):
        adapter_props = dbus.Interface(self.adapter, 'org.freedesktop.DBus.Properties')
        adapter_props.Set('org.bluez.Adapter1', 'Powered', dbus.Boolean(1))
        adapter_props.Set('org.bluez.Adapter1', 'Alias', dbus.String(DEVICE_NAME))
        os.system("bluetoothctl discoverable on")
        os.system("bluetoothctl pairable on")
        os.system("bluetoothctl agent NoInputNoOutput")
        os.system("bluetoothctl default-agent")

    def send_report(self, report):
        # Placeholder for sending HID report over Bluetooth
        pass

def find_keyboard_device():
    for dev in hid.enumerate():
        if dev['usage_page'] == 0x01 and (dev['usage'] == 0x06 or dev['usage'] == 0x02):
            return dev['path']
    return None

def passthrough_loop(bt):
    while True:
        try:
            dev_path = find_keyboard_device()
            if not dev_path:
                print("No HID device found, retrying...")
                time.sleep(1)
                continue

            with hid.Device(path=dev_path) as device:
                print(f"Connected to HID device: {device}")
                while True:
                    report = device.read(64)
                    if report:
                        bt.send_report(report)
                    time.sleep(HID_POLL_INTERVAL)

        except Exception as e:
            print(f"Error in passthrough loop: {e}")
            time.sleep(2)

def main():
    bt = BluetoothHID()
    bt.setup_device()
    passthrough_loop(bt)

if __name__ == "__main__":
    main()
