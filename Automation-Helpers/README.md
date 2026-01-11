## 1. Overview

**`GitExporttoyaml.py`** is a Python automation script designed to scan a specified directory for Git repositories and generate a system profile in YAML format. This profile, referred to as the "System-DNA," serves as a manifest of the development environment.

The script systematically iterates through subdirectories of a defined base path, identifies Git repositories, and extracts key metadata for each, including the repository's name, local path, remote URL, and the currently active branch.

This information is aggregated along with system-level context—such as a system identifier, export timestamp, and environment details—and then exported to a structured YAML file. The resulting `system_profile.yaml` provides a clear and version-controllable snapshot of the workspace configuration.

## 2. Prerequisites

### 2.1. Software Requirements

-   **Python 3.6+:** The script is written in Python and requires a compatible interpreter.
-   **Git:** The Git command-line interface (CLI) must be installed and accessible in the system's `PATH`. The script relies on `git` commands to introspect repository details.
-   **PyYAML Library:** The script uses the `PyYAML` library to serialize data into YAML format. It can be installed via pip:
    ```bash
    pip install pyyaml
    ```

### 2.2. Environment Configuration

-   **Directory Structure:** The script expects a specific directory structure. The `base_path` variable is hardcoded to `C:\Git` and the output directory for the YAML file is hardcoded to `C:\Git\OPS-Systems\`. Ensure these paths exist or modify the script variables to match your environment.

## 3. Usage

### 3.1. Execution

To execute the script, navigate to its location in a terminal and run it using the Python interpreter:

```bash
python GitExporttoyaml.py
```

Upon successful execution, the script will print a confirmation message to the console, indicating the path of the exported YAML file:

```
✅ System-DNA erfolgreich nach C:\Git\OPS-Systems\system_profile.yaml exportiert.
```

### 3.2. Configuration

The script's behavior can be customized by modifying the following variables at the beginning of the file:

-   `base_path`: Defines the root directory to be scanned for Git repositories.
    -   **Default:** `"C:\\Git"`
-   `export_file`: Defines the full path, including the filename, for the output YAML file.
    -   **Default:** `os.path.join(base_path, "OPS-Systems", "system_profile.yaml")`

### 3.3. Output File

The script generates a YAML file (`system_profile.yaml`) with the following structure:

```yaml
system_identity: Jarvis-Core / OPS-Samurai
export_date: '2023-10-27 10:00:00'
environment:
  workspace_root: C:\Git
  powershell_profile: C:\Git\OPS-Systems\Windows-Core\profile.ps1
  os_compatibility:
  - PowerShell 5.1
  - PowerShell 7.5.4
repositories:
- name: MyFirstRepo
  path: C:\Git\MyFirstRepo
  remote: https://github.com/user/myfirstrepo.git
  active_branch: main
- name: AnotherProject
  path: C:\Git\AnotherProject
  remote: https://github.com/user/anotherproject.git
  active_branch: develop
```
