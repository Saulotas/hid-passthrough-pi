#!/usr/bin/env python3
import os
import time
import yaml
import subprocess

# Load configuration
with open('/opt/hid-passthrough/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

OTA_ENABLED = config.get('ota_enabled', True)
OTA_REPO_URL = config.get('ota_repo_url', '')
OTA_CHECK_INTERVAL = config.get('ota_check_interval', 24) * 3600  # convert hours to seconds

def git_pull():
    try:
        print("[OTA] Checking for updates...")
        cwd = '/opt/hid-passthrough/'
        result = subprocess.run(['git', 'pull'], cwd=cwd, capture_output=True, text=True)
        if "Already up to date." not in result.stdout:
            print("[OTA] Update found! Restarting services...")
            os.system("sudo systemctl restart hid_passthrough.service")
            os.system("sudo systemctl restart bt_autopair.service")
            os.system("sudo systemctl restart bt_led_status.service")
    except Exception as e:
        print(f"[OTA] Error checking for updates: {e}")

def setup_git_repo():
    if not os.path.exists('/opt/hid-passthrough/.git'):
        try:
            print("[OTA] Cloning fresh repo...")
            os.system(f"sudo git clone {OTA_REPO_URL} /opt/hid-passthrough/")
        except Exception as e:
            print(f"[OTA] Failed initial clone: {e}")

def main():
    if not OTA_ENABLED:
        print("[OTA] OTA updates are disabled in config.yaml")
        return

    setup_git_repo()

    while True:
        git_pull()
        time.sleep(OTA_CHECK_INTERVAL)

if __name__ == "__main__":
    main()
