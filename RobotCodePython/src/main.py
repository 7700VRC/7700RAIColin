# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       homunculus                                                   #
# 	Created:      3/24/2024, 3:15:08 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
brain_inertial = Inertial(3)
cin = DigitalIn(4)
cout = DigitalOut(4)

vendor_id = 0
product_id = 0

# VEX Python program to read inputs from a computer

def read():
    numOfDataEntries = 100
    pollingDelayMsec = 50
    dataBuffer = ""

    brain.timer.clear()

    # iterate through certain amoount
    for i in range(0,numOfDataEntries):

        # log data to buffer
        dataBuffer += "%1.3f" % brain.timer.value() + "/n"
        dataBuffer += "%1.3f" % brain_inertial.acceleration(XAXIS) + "/n"
        
        wait(pollingDelayMsec, MSEC)

# Main function
def main():
    read()

if __name__ == "__main__":
    main()
