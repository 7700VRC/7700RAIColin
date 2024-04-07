/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       homunculus                                                */
/*    Created:      4/7/2024, 2:29:23 PM                                      */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/
#include "vex.h"
#include "iostream"

using namespace vex;
using namespace std;

// A global instance of vex::brain used for printing to the V5 brain screen
brain Brain;
ai::jetson jetson

// define your global instances of motors and other devices here


int main() {
   
    cout << "1" << endl;

    while(1) {
        // Allow other tasks to run
        wait(10, msec);
    }
}
