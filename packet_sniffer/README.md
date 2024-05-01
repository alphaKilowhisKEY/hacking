# HTTP Packet Sniffer

This Python script allows you to sniff HTTP packets on a specified network interface using Scapy library. 
It can extract URLs and potential login information from the captured packets and log them into a file.

- Captures HTTP packets on the specified interface.
- Extracts URLs and potential login information from the packets.
- Logs the captured data into log files for further analysis.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)

## Usage
$ python3 main.py

### Options
-l, --logging: Specify whether logging is enabled or not. Provide true or false.

## Example
$ python3 main.py -l true

**Note:** This script is for educational purposes only. Misuse of this script may be illegal and unethical. Use it responsibly and only on networks you have permission to test. The authors of these scripts are not responsible for any misuse or damage caused by the scripts.
