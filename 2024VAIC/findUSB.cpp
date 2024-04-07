#include <iostream>
#include <libusb-1.0/libusb.h>

int main() {
    libusb_context *ctx = nullptr;
    libusb_device **devs;
    ssize_t num_devs;

    // Initialize libusb
    if (libusb_init(&ctx) != LIBUSB_SUCCESS) {
        std::cerr << "Failed to initialize libusb" << std::endl;
        return 1;
    }

    // Get the list of USB devices
    num_devs = libusb_get_device_list(ctx, &devs);
    if (num_devs < 0) {
        std::cerr << "Failed to get USB device list" << std::endl;
        libusb_exit(ctx);
        return 1;
    }

    // Iterate through the devices and print their vendor and product IDs
    for (ssize_t i = 0; i < num_devs; ++i) {
        libusb_device *dev = devs[i];
        struct libusb_device_descriptor desc;

        // Get device descriptor
        if (libusb_get_device_descriptor(dev, &desc) != LIBUSB_SUCCESS) {
            std::cerr << "Failed to get device descriptor" << std::endl;
            continue;
        }

        // Print vendor and product IDs
        std::cout << "Vendor ID: 0x" << std::hex << static_cast<unsigned int>(desc.idVendor)
                  << " Product ID: 0x" << std::hex << static_cast<unsigned int>(desc.idProduct) << std::endl;
    }

    // Free the device list
    libusb_free_device_list(devs, 1);

    // Exit libusb
    libusb_exit(ctx);

    return 0;
}
