# Custom Tools

## Description
This Python script provides a set of custom tools for managing devices and performing various operations. 
Users can interact with the tools through a command-line interface.

### Why changing MAC address?
1. Increase anonymity
2. Impersonate other devices.
3. Bypass filters.

## Features
- **List Available Commands**: Display all available commands to the user.
- **List All Names**: List all device names currently available.
- **Change Device Name**: Change the name or MAC address of a specific device.
- **Exit**: Terminate the program and exit the command-line interface.

## Usage
1. Run the script to start the command-line interface.
2. Enter one of the available commands listed.
3. Follow the prompts and input any required information.
4. Perform operations such as listing device names, changing device names, or exiting the program.

## Requirements
- Python 3.x

## Files
- **tools.py**: Defines the custom tools and functions used in the script.
- **main.py**: The main script that runs the command-line interface and interacts with the tools.

## How to change MAC address manually

$ ifconfig [to list all devices.]

$ ifconfig eth0 down [to disable the interface eth0]

$ifconfig eth0 hw ether 00:11:22:33:44:55 [to change the name]

$ ifconfig eth0 up [to enable the interface eth0]

$ ifconfig [to check if the name was changed]