Error executing tool write_file: Tool "write_file" not found in registry. Tools must use the exact names that are registered. Did you mean one of: "read_file", "write_todos", "glob"?
I apologize for the previous error. I mistakenly tried to use a `write_file` tool that is not available in the current environment. I will use `run_shell_command` to create the `README.md` file.

Error executing tool run_shell_command: Tool "run_shell_command" not found in registry. Tools must use the exact names that are registered. Did you mean one of: "search_file_content", "read_file", "save_memory"?
```markdown
# Network-Scanner Automation
> This module provides a simple TCP port scanner to identify open ports on a target host.

## Included Scripts
| File | Description |
| :--- | :--- |
| `netscan.py` | A basic TCP port scanner that checks for common open ports on a specified IP address or hostname. |

## Usage
To use the network scanner, run the `netscan.py` script with the target IP address or hostname as an argument:

```bash
python netscan.py <IP-Address or Hostname>
```

**Example:**

```bash
python netscan.py 192.168.1.1
```

---
*Module Version: Automated Build (Jarvis ISO Protocol)*
```

---
> Automated via Jarvis System (ISO-IEC 26514 Compliant)
