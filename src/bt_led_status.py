#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
import subprocess
import yaml

# Load configuration
with open('/opt/hid-passthrough/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

LED_PIN = config.get('led_pin', -1)

def setup_led():
    if LED_PIN >= 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)

def led_on():
    if LED_PIN >= 0:
        GPIO.output(LED_PIN, GPIO.HIGH)

def led_off():
    if LED_PIN >= 0:
        GPIO.output(LED_PIN, GPIO.LOW)

def check_connected():
    try:
        output = subprocess.check_output("bluetoothctl info", shell=True).decode()
        if "Connected: yes" in output:
            return True
    except Exception as e:
        print(f"[BT LED Status] Error checking connection: {e}")
    return False

def main():
    setup_led()
    while True:
        connected = check_connected()
        if connected:
            led_on()
        else:
            led_off()
        time.sleep(2)

if __name__ == "__main__":
    main()
