/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       homunculus                                                */
/*    Created:      3/24/2024, 1:30:59 PM                                     */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/
#include "vex.h"
#include <libusb-1.0/libusb.h>

using namespace vex;
using namespace std;

// A global instance of vex::brain used for printing to the V5 brain screen
brain Brain;

// define your global instances of motors and other devices here


int main() {
    libusb_device_handle *handle;
    libusb_context *ctx = NULL;
    int ret;
}
