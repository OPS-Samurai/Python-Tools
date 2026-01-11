# 💻 netscan.py Control Module
> Simple TCP Port Scanner (Python). This script performs a basic scan of common TCP ports on a specified target IP address or hostname.

## 🛠️ Prerequisites
- Python 3.x
- Standard Python libraries: `socket`, `sys`, `datetime`

## ⚙️ Technical Details
The `netscan.py` script functions as a command-line TCP port scanner. It resolves the hostname of the target to an IP address and then attempts to connect to a predefined list of common ports using TCP sockets.

**Key functionalities:**
- **Hostname Resolution:** Utilizes `socket.gethostbyname()` to convert a given hostname into its corresponding IPv4 address.
- **Socket Creation:** For each port in the predefined list, a new `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` is created, specifying IPv4 and TCP protocol.
- **Connection Attempt:** The `connect_ex()` method is used to attempt a connection to the target IP and port. A return value of `0` indicates a successful (open) connection.
- **Service Identification:** If a port is found to be open, the script attempts to identify the associated service name using `socket.getservbyport()`.
- **Timeout:** A default timeout of 0.5 seconds is set for each connection attempt to ensure the scan completes in a reasonable time.
- **Error Handling:** The script includes basic error handling for hostname resolution failures, network connection issues, and user-initiated scan cancellations (`KeyboardInterrupt`).

**Ports Scanned:**
The script targets the following common TCP ports: 21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 139 (NetBIOS Session Service), 443 (HTTPS), 445 (SMB), 3389 (RDP), and 8080 (HTTP Proxy/Alternate HTTP).

## 🚀 Usage Protocols
To use the `netscan.py` script, execute it from the command line, providing the target IP address or hostname as an argument.

**Command Line:**
```bash
python netscan.py <IP-Adresse oder Hostname>
```

**Example:**
To scan the host `example.com`:
```bash
python netscan.py example.com
```

To scan the IP address `192.168.1.1`:
```bash
python netscan.py 192.168.1.1
```
