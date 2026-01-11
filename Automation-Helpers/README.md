Error executing tool write_file: Tool "write_file" not found in registry. Tools must use the exact names that are registered. Did you mean one of: "read_file", "write_todos", "glob"?
Error executing tool write_file: Tool "write_file" not found in registry. Tools must use the exact names that are registered. Did you mean one of: "read_file", "write_todos", "glob"?
```markdown
# Automation-Helpers Automation
> This module contains scripts designed to automate system information gathering and configuration tasks, specifically focusing on Git repository metadata export to YAML.

## Included Scripts
| File | Description |
| :--- | :--- |
| GitExporttoyaml.py | Scans a predefined base directory (`C:\Git`) for Git repositories, retrieves their active branch and remote URL, and exports a comprehensive system profile, including environment details and repository metadata, into a `system_profile.yaml` file located at `C:\Git\OPS-Systems\system_profile.yaml`. |

## Usage
This script is designed to be executed directly. It operates on hardcoded paths for the base workspace and the output file, requiring no command-line arguments.

```python
python GitExporttoyaml.py
```

---
*Module Version: Automated Build (Jarvis ISO Protocol)*
```

---
> Automated via Jarvis System (ISO-IEC 26514 Compliant)
