# 💻 Netscan Control Module
> This module provides a simple TCP port scanner functionality written in Python.

## 🛠️ Prerequisites
- Python 3.x
- Standard Python libraries (`socket`, `sys`, `datetime`). No additional installations are required.

## ⚙️ Technical Details
The `netscan.py` script implements a basic TCP port scanner. It leverages Python's `socket` module to perform network operations.
- **Hostname Resolution**: The script first attempts to resolve the provided target hostname to an IPv4 address using `socket.gethostbyname()`. If resolution fails, an error is reported, and the scan is aborted.
- **Port Scanning**: It iterates through a predefined list of common ports (21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080). For each port:
    - A new `AF_INET` (IPv4) `SOCK_STREAM` (TCP) socket is created.
    - A default timeout of 0.5 seconds is set using `socket.setdefaulttimeout()`.
    - `s.connect_ex()` is used to attempt a connection. A return value of 0 indicates a successful (open) connection.
    - If a port is open, the script attempts to identify the associated service using `socket.getservbyport()`.
    - The socket is closed after each port check.
- **Error Handling**: The script includes basic error handling for:
    - `socket.gaierror`: Hostname resolution failures.
    - `KeyboardInterrupt`: User abortion of the scan.
    - `socket.error`: General network connection issues.

## 🚀 Usage Protocols
The script is executed from the command line and requires one argument: the target IP address or hostname to scan.

**Syntax:**
```bash
python netscan.py <IP-Adresse oder Hostname>
```

**Example:**
To scan a target with the IP address `192.168.1.1`:
```bash
python netscan.py 192.168.1.1
```
To scan a target with the hostname `example.com`:
```bash
python netscan.py example.com
```
