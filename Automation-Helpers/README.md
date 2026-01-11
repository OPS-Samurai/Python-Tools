# 📝 GitExporttoyaml.py
> This script scans a specified base directory for Git repositories, extracts their metadata, and exports this information into a structured YAML manifest file.

## 🛠️ Prerequisites
- **Python 3.x**
- **PyYAML Library**: Required for YAML serialization. Install via pip: `pip install pyyaml`
- **Git**: Must be installed and accessible in the system's PATH for repository introspection.

## ⚙️ Technical Details
The script performs the following operations:
1.  **Initialization**: It defines a static base path `C:\Git` as the root directory for scanning. A manifest dictionary is created with metadata, including a static `system_identity`, the export timestamp, and predefined environment details.
2.  **Git Repository Discovery**: It iterates through each item in the base path. For each subdirectory, it attempts to execute `git` commands (`git branch --show-current`, `git remote get-url origin`) to determine the active branch and remote origin URL. If a directory is not a Git repository or the commands fail, it gracefully assigns default values.
3.  **Data Aggregation**: Information for each discovered repository—including its name, local path, remote URL, and active branch—is appended to the `repositories` list within the main manifest.
4.  **YAML Export**: The complete manifest data structure is serialized into a YAML file named `system_profile.yaml`. This file is written to a hardcoded path: `C:\Git\OPS-Systems\system_profile.yaml`.

## 🚀 Usage
Execute the script from the command line. No arguments are required.

```bash
python GitExporttoyaml.py
```

Upon successful execution, the script will print a confirmation message to the console and create the `system_profile.yaml` file at the designated export location.
