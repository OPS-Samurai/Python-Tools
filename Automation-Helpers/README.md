# 💻 GitExporttoyaml.py Control Module
## 🛠️ Prerequisites
- Python 3.x environment
- `PyYAML` library for YAML serialization.
- `git` command-line interface (CLI) installed and accessible in the system's PATH.

## ⚙️ Technical Details
The module is designed to scan a specified base directory (`C:\Git`) for Git repositories. It performs the following operations:

1.  **Git Information Retrieval**: A function `get_git_info` uses the `subprocess` module to execute `git` commands. It captures the current branch (`git branch --show-current`) and the origin remote URL (`git remote get-url origin`) for a given directory path. It includes error handling for directories that are not Git repositories.
2.  **Manifest Generation**: It initializes a dictionary object named `manifest`. This structure is populated with static metadata, including a `system_identity`, the `export_date` (current timestamp), and `environment` details such as the workspace root.
3.  **Repository Scanning**: The script iterates through all items in the hardcoded `base_path`. For each item that is a directory, it invokes `get_git_info` to collect repository details.
4.  **Data Aggregation**: The details for each discovered repository—including its name, local path, remote URL, and active branch—are appended to the `repositories` list within the `manifest`.
5.  **YAML Export**: The fully populated `manifest` dictionary is serialized into a YAML format. The output is written to a hardcoded file path: `C:\Git\OPS-Systems\system_profile.yaml`, overwriting any existing file. A confirmation message is printed to standard output upon successful export.

## 🚀 Usage Protocols
Execute the script from a terminal using the Python interpreter. No command-line arguments are required as all paths are hardcoded within the script.

```bash
python GitExporttoyaml.py
```

Upon successful execution, the script will create or update the `system_profile.yaml` file and print a confirmation message.
