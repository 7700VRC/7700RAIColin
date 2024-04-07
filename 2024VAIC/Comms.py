import usb.core
import usb.util 

# Find USB device by vendor ID and product ID
vendor_id = 10376  # Replace with your USB device's vendor ID
product_id = 1281  # Replace with your USB device's product ID

# Find the device
device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

# If the device is not found, exit
if device is not None:
    print(device)
elif device is None:
    print("Device not found")
    exit()

while True:
    # Detach kernel driver if it's active
    if device.is_kernel_driver_active(0):
        device.detach_kernel_driver(0)

    # Set the active configuration. With no arguments, the first configuration will be the active one
    device.set_configuration()

    # Get an endpoint instance
    endpoint = device[0][(0, 0)][0]

    # Data to be sent to the device (if any)
    data_to_send = b'\x01\x02\x03\x04'

    # Write data to the device
    if data_to_send:
        device.write(endpoint.bEndpointAddress, data_to_send)

    # Read data from the device
    data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

    # Print the received data
    print("Received data:", data)

# Release the interface
usb.util.release_interface(device, 0)

# Reattach the kernel driver
device.attach_kernel_driver(0)

# Reset the device
device.reset()