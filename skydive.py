import matplotlib.pyplot as plt
import numpy as np
from pint import UnitRegistry
import argparse
import os

# Initialize plot
plt.rcParams['figure.figsize'] = [20, 10]


ureg = UnitRegistry()
Q_ = ureg.Quantity

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action = "store_true")
parser.add_argument("infile", nargs="?", type=argparse.FileType('r'), help="file to read measurements from", default=None)
args = parser.parse_args()

if args.verbose: print("Assigning default arguments")
measurements = {
    "g": ureg("9.8 meters/second**2"),
    "mass": ureg("100 kilograms"),
    "step": ureg("0.1 seconds"),
    "height": ureg("3000 meters"),
    "parachute_height": ureg("1000 meters") 
}

# TODO read from file
if infile is not None:
	if args.verbose: print("Input file recognized; validating...")
    if os.path.isfile(args.infile):
		if args.verbose: print("Input file validated")
    else:
        raise FileNotFoundError(string)
    with open(infile):
        g = ureg(   

if args.verbose: print("Initializing arguments")
time = Q_(0, ureg.second)
speed = Q_(0, ureg.meter / ureg.second)
parachute = False
t = [time]

# Main Loop
if args.verbose: print("Starting main loop")
while height <= 0:
    speed -= g * step
    #TODO calculate height
    #height += 
    time += step
    #TODO parachute
    #if !parachute && height <= parachute_height:
        
#TODO plot
#fig, axs = plt.subplots(2, 2)
#axs[0, 0].plot(t, h)
#axs[0, 0].set_title('write your title here')
#axs[0, 0].set(xlabel='something with unts',ylabel='something else with units')
