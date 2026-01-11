# 💻 netscan Control Module
## 🛠️ Prerequisites
This script requires a Python 3 environment.

## ⚙️ Technical Details
The `netscan` control module implements a basic TCP port scanner. It is designed to scan a specified target (IP address or hostname) for a predefined list of common open TCP ports.

**Core Functionality:**
*   **Hostname Resolution:** Utilizes `socket.gethostbyname` to resolve a given hostname into its corresponding IPv4 address.
*   **Port Scanning:** Iterates through a fixed set of "Big 10" ports: 21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 139 (NetBIOS Session Service), 443 (HTTPS), 445 (SMB), 3389 (RDP), and 8080 (HTTP Proxy/Alternate HTTP).
*   **Socket Management:** Employs `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` to create IPv4 TCP sockets for connection attempts.
*   **Connection Timeout:** Sets a default socket timeout of 0.5 seconds for quick scan results.
*   **Port Status Check:** Uses `s.connect_ex((target_ip, port))` to attempt a connection, where a return value of 0 indicates an open port.
*   **Service Identification:** Attempts to identify the service running on an open port using `socket.getservbyport`.
*   **Error Handling:** Includes basic error handling for hostname resolution failures, user-initiated cancellations (`KeyboardInterrupt`), and general socket errors (e.g., no connection to server).

## 🚀 Usage Protocols
To use the `netscan` module, execute it from the command line, providing a target IP address or hostname as an argument.

**Command Line Interface (CLI):**
`python netscan.py <IP-Adresse oder Hostname>`

**Example:**
To scan the host `example.com`:
`python netscan.py example.com`

To scan the IP address `192.168.1.1`:
`python netscan.py 192.168.1.1`
