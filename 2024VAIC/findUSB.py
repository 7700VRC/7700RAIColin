import usb.core

def scan_usb_devices():
    # Find all USB devces
    devices = usb.core.find(find_all=True)
    
    if devices is None:
        print("No USB devices found.")
        return
    
    print("USB Devices Found:")
    print("------------------")
    
    for device in devices:
        vendor_id = device.idVendor
        product_id = device.idProduct
        
        print(f"Vendor ID: {vendor_id}, Product ID: {product_id}")
    
    print("------------------")

if __name__ == "__main__":
    scan_usb_devices()
