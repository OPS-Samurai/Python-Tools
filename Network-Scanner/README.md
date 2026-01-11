# 💻 netscan.py Control Module
## 🛠️ Prerequisites
- Python 3 environment.
- Standard libraries: `socket`, `sys`, `datetime`. No external packages are required.

## ⚙️ Technical Details
The module operates as a basic TCP port scanner. Upon execution, it accepts a target host, specified as either an IP address or a fully qualified domain name (FQDN).

1.  **Hostname Resolution**: The script first attempts to resolve the provided hostname to an IPv4 address using `socket.gethostbyname()`. If resolution fails, it terminates with an error message.
2.  **Socket Configuration**: A standard IPv4 TCP socket (`socket.AF_INET`, `socket.SOCK_STREAM`) is instantiated for each port check. A default timeout of 0.5 seconds is set for all socket operations to ensure rapid scanning.
3.  **Port Scanning**: The module iterates through a predefined list of common TCP ports: 21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, and 8080.
4.  **Connection Test**: For each port, it uses `socket.connect_ex()` to attempt a connection. A return value of `0` signifies that the port is open.
5.  **Service Identification**: If a port is found to be open, the script attempts to identify the associated service using `socket.getservbyport()`. If the service cannot be determined, it is labeled as "Unknown".
6.  **Exception Handling**: The process includes handlers for `KeyboardInterrupt` to allow graceful shutdown by the user and `socket.error` for connection-related failures.

## 🚀 Usage Protocols
The script must be executed via a command-line interface.

**Syntax:**
```bash
python netscan.py <target_host>
```

**Arguments:**
-   `<target_host>`: The IP address or hostname to be scanned.

**Example:**
```bash
python netscan.py 192.168.1.1
```
or
```bash
python netscan.py example.com
```
