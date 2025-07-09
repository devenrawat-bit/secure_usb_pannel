import wmi
#this code worked well for both keyboard and phone via usb when connected
def list_all_usb_devices():
    c = wmi.WMI()
    print("\n📦 Scanning Connected USB Devices:\n")

    for device in c.Win32_PnPEntity():
        if device.PNPDeviceID and "USB" in device.PNPDeviceID:
            print("-" * 50)
            print(f"🔹 Name           : {device.Name}")
            print(f"🔹 Device ID      : {device.DeviceID}")
            print(f"🔹 Manufacturer   : {device.Manufacturer}")
            print(f"🔹 PNP Device ID  : {device.PNPDeviceID}")
            print(f"🔹 Status         : {device.Status}")

if __name__ == "__main__":
    list_all_usb_devices()

#     ✅ What does Status: OK mean in WMI?
# The Status property comes from WMI's Win32_PnPEntity class, and here's what it tells you:

# "OK" → The device is functioning properly according to Windows.

# "Error" or other statuses → There’s a problem with the device like missing drivers, resource conflicts, etc.

# ⚠️ But: "OK" only means "Windows recognizes it and the driver is working."
# It does not mean the device is safe or not malicious.


