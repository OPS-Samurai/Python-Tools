# 💻 GitExporttoyaml.py Control Module

## 🛠️ Prerequisites

- **Python Environment**: Requires a standard Python installation.
- **Libraries**: The script utilizes the following standard Python libraries:
    - `os`: For interacting with the operating system, primarily for path manipulation and directory listing.
    - `yaml`: For serializing the collected data into YAML format. Must be installed (e.g., `pip install pyyaml`).
    - `subprocess`: To execute external `git` commands.
    - `datetime`: To generate a timestamp for the export.
- **System Dependencies**: A functional `git` client must be installed and accessible via the system's command-line PATH.

## ⚙️ Technical Details

The module is designed to catalog Git repositories within a specified base directory and export this information into a structured YAML file.

- **`get_git_info(path)` Function**:
    - This function takes a directory path as input.
    - It executes `git branch --show-current` and `git remote get-url origin` commands within the specified path to retrieve the active branch and the remote URL.
    - It includes error handling to return default values ("unknown" branch, "none" remote) if the directory is not a valid Git repository or if the commands fail.

- **Manifest Structure**:
    - A primary dictionary named `manifest` is initialized to store the system's state.
    - It contains static metadata such as `system_identity`, `export_date`, and `environment` details, including the workspace root and compatible OS shells.
    - A `repositories` key is initialized as an empty list to be populated with discovered repository data.

- **Core Logic**:
    - The script defines a hardcoded `base_path` (`C:\\Git`) as the target for scanning.
    - It iterates through all items in the `base_path`. For each item that is a directory, it invokes the `get_git_info` function.
    - The retrieved repository information (name, path, remote URL, active branch) is appended as a dictionary to the `manifest["repositories"]` list.

- **Export Process**:
    - The final `manifest` dictionary is serialized into a YAML file.
    - The output destination is hardcoded to `C:\\Git\\OPS-Systems\\system_profile.yaml`.
    - Upon successful file creation, a confirmation message is printed to the standard output.

## 🚀 Usage Protocols

Execute the script from a Python interpreter. No command-line arguments are required.

```bash
python GitExporttoyaml.py
```

The primary function is to perform a system reconnaissance of the `C:\\Git` directory, gather metadata on all contained Git repositories, and consolidate this data into a single `system_profile.yaml` file for system state analysis.
