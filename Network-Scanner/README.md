# Network-Scanner Module

## Overview
This script, `netscan.py`, is a simple TCP port scanner written in Python. It scans the "big 10" ports for a specified target IP address or hostname.

## Usage
Run the script with the following command:
```
python netscan.py <IP-Adresse oder Hostname>
```
Replace `<IP-Adresse oder Hostname>` with the desired target IP address or hostname.

## Features

* Scans the "big 10" ports (21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080)
* Provides information on open and closed ports
* Supports IPv4 addresses and hostnames

## Limitations
The script has the following limitations:
* It only scans the "big 10" ports and does not support custom port scanning.
* It uses a default timeout of 0.5 seconds for each connection attempt.

## Troubleshooting
If you encounter any issues while running the script, refer to the following:

* Error: Hostname could not be resolved. Check that the hostname is correctly spelled and try again.
* Error: Could not connect to the server. Check your network connection and try again.

## Credits
The script was written by [Your Name].

## License
This script is licensed under the MIT License.

---
> All systems are managed under ISO/IEC 26514 compliant documentation standards via Local AI.
