import wmi
import re
#more finalized 
def is_external_device(name, manufacturer, pnp_id):
    name = (name or "").lower()
    manufacturer = (manufacturer or "").lower()
    pnp_id = (pnp_id or "").lower()

    # Known internal indicators
    internal_keywords = ['hub', 'camera', 'bluetooth', 'root', 'infrared', 'webcam']
    known_internal_makers = [
        'microsoft', 'realtek', 'standard usb host controller', 
        'standard system devices', '(standard usb hubs)'
    ]
    known_internal_names = ['usb composite device']

    # Known external manufacturers
    known_external_makers = ['xiaomi', 'samsung', 'oneplus', 'vivo', 'oppo', 'realme', 'kingston', 'sandisk', 'toshiba', 'seagate', 'wd', 'transcend', 'sony']

    # Known external device VIDs
    known_external_vids = [
        'vid_2717', 'vid_04e8', 'vid_2a70', 'vid_2a45', 'vid_0bb4',
        'vid_0781', 'vid_0951', 'vid_0bc2', 'vid_1058', 'vid_054c', 'vid_8564', 'vid_0930'
    ]

    # External keywords in device name
    external_keywords = ['mass storage', 'phone', 'mtp', 'removable', 'usb device']

    if name in known_internal_names:
        return False
    if any(word in name for word in internal_keywords):
        return False
    if manufacturer in known_internal_makers:
        return False
    if 'root_hub' in pnp_id or 'hub' in pnp_id:
        return False
    if manufacturer in known_external_makers:
        return True
    if any(vid in pnp_id for vid in known_external_vids):
        return True
    if any(word in name for word in external_keywords):
        return True
    if 'mtp' in pnp_id or 'mass' in pnp_id or 'storage' in pnp_id:
        return True

    return False

def list_all_usb_devices():
    c = wmi.WMI()
    print("\n📦 Scanning Connected USB Devices:\n")

    for device in c.Win32_PnPEntity():
        if device.PNPDeviceID and "USB" in device.PNPDeviceID:
            name = device.Name
            manufacturer = device.Manufacturer
            pnp_id = device.PNPDeviceID

            device_type = "External" if is_external_device(name, manufacturer, pnp_id) else "Internal"

            print("-" * 50)
            print(f"🔹 Name           : {name}")
            print(f"🔹 Device Type    : {device_type}")
            print(f"🔹 Device ID      : {device.DeviceID}")
            print(f"🔹 Manufacturer   : {manufacturer}")
            print(f"🔹 PNP Device ID  : {pnp_id}")
            print(f"🔹 Status         : {device.Status}")

if __name__ == "__main__":
    list_all_usb_devices()
