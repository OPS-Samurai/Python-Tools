# 📝 Network Scanner Script
## 🛠️ Prerequisites
This script requires Python 3 to run. It utilizes standard Python libraries (`socket`, `sys`, `datetime`) which are included with a standard Python installation.
## ⚙️ Technical Details
The `netscan.py` script implements a basic TCP port scanner. It defines a `scan_target` function that takes a target (IP address or hostname) as an argument.

Key functionalities include:
- **Hostname Resolution**: Attempts to resolve the provided target hostname to an IP address using `socket.gethostbyname()`.
- **Port Scanning**: Iterates through a predefined list of common TCP ports (21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080).
- **Socket Connection**: For each port, it creates an IPv4 TCP socket (`socket.AF_INET`, `socket.SOCK_STREAM`) and sets a default timeout of 0.5 seconds.
- **Connection Check**: Uses `s.connect_ex()` to attempt a connection, returning 0 on success (port open) or an error code otherwise.
- **Service Identification**: For open ports, it attempts to identify the service using `socket.getservbyport()`.
- **Error Handling**: Includes exception handling for `socket.gaierror` (hostname resolution failure), `KeyboardInterrupt` (user abortion), and `socket.error` (general connection issues).
- **Output**: Provides formatted output indicating the target, start time, and status of each scanned port (OPEN/CLOSED) along with the service name if identified.
## 🚀 Usage (Examples)
To use the script, provide a target IP address or hostname as a command-line argument.

```bash
python netscan.py <IP-Adresse oder Hostname>
```

**Example:**
```bash
python netscan.py 192.168.1.1
```
or
```bash
python netscan.py example.com
```
