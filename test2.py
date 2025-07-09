def is_external_device(name, manufacturer, pnp_id):
    name = (name or "").lower()
    manufacturer = (manufacturer or "").lower()
    pnp_id = (pnp_id or "").lower()

    # Keywords that usually indicate internal devices
    internal_keywords = ['hub', 'camera', 'bluetooth', 'root', 'infrared', 'webcam']
    known_internal_makers = ['microsoft', 'realtek', 'standard usb host controller', 'standard system devices', '(standard usb hubs)']

    # External device indicators
    external_keywords = ['mass storage', 'phone', 'mtp', 'removable', 'usb device']

    # If it matches internal patterns → treat as internal
    if any(word in name for word in internal_keywords):
        return False
    if manufacturer in known_internal_makers:
        return False
    if 'root_hub' in pnp_id or 'hub' in pnp_id:
        return False

    # If it matches external indicators → treat as external
    if any(word in name for word in external_keywords):
        return True
    if 'mtp' in pnp_id or 'vid_0' in pnp_id:
        return True

    # If it doesn’t match anything, assume internal for safety
    return False
