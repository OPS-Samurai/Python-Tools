## 1. Overview

This document describes the `netscan.py` utility, a command-line tool for network diagnostics. It is a lightweight and efficient TCP port scanner designed to determine which of the most common ports are open on a given network host.

The script performs the following key functions:
-   Resolves a target hostname to its corresponding IPv4 address.
-   Scans a predefined list of commonly used TCP ports: 21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, and 8080.
-   Reports the status of each open port and attempts to identify the associated service (e.g., HTTP, FTP, SSH).
-   Provides clear start and end timestamps for the scanning operation.

This tool is intended for network administrators and security professionals for basic network reconnaissance and service verification.

## 2. Prerequisites

To run the `netscan.py` script, the following requirements must be met:

-   **Python:** Python 3.x must be installed on the system.
-   **Standard Libraries:** The script relies solely on standard Python libraries (`socket`, `sys`, `datetime`) and requires no external packages to be installed.
-   **Network Access:** The host machine must have network connectivity to the target system. Firewalls or other network security measures may block the scan and affect the results.

## 3. Usage

The script is executed from the command line.

### Syntax

```sh
python netscan.py <target>
```

-   `<target>`: The IP address or fully qualified hostname of the system you wish to scan.

### Example

To scan the host `example.com`, use the following command:

```sh
python netscan.py example.com
```

### Output

The script will produce output similar to the following, listing any open ports it discovers within its predefined list.

```
--------------------------------------------------
🎯 Ziel: 93.184.216.34
🕒 Start: 2026-01-11 10:30:00.123456
--------------------------------------------------
✅ Port    80/tcp OFFEN  (http)
✅ Port   443/tcp OFFEN  (https)
--------------------------------------------------
🏁 Scan abgeschlossen.
```
