# 💻 GitExporttoyaml Control Module

## 🛠️ Prerequisites

- **Python Environment**: A standard Python 3 installation is required.
- **Git**: The Git command-line interface (CLI) must be installed and accessible in the system's PATH.
- **PyYAML Library**: The script depends on the `PyYAML` library for YAML serialization. It can be installed via pip:
  ```sh
  pip install PyYAML
  ```

## ⚙️ Technical Details

The module is designed to scan a predefined directory for Git repositories and generate a system profile in YAML format.

- **Core Functionality**: It defines a `get_git_info` function that executes `git` commands (`git branch --show-current`, `git remote get-url origin`) using the `subprocess` module to retrieve the active branch and remote origin URL for a given repository path.
- **Data Structure**: A primary dictionary object, `manifest`, is initialized to structure the output. It includes static metadata such as `system_identity` and `environment`, a dynamic `export_date`, and an empty list for `repositories`.
- **Repository Scanning**: The script iterates through all top-level folders within the hardcoded `base_path` (`C:\\Git`). For each folder, it invokes `get_git_info` and appends the folder name, path, remote URL, and active branch to the `repositories` list.
- **Error Handling**: A `try...except` block within `get_git_info` manages directories that are not valid Git repositories, assigning default values of `"unknown"` for the branch and `"none"` for the remote.
- **Output Generation**: The final `manifest` dictionary is serialized into a human-readable YAML file using `yaml.dump`. The output is written to a hardcoded location: `C:\\Git\\OPS-Systems\\system_profile.yaml`.
- **Confirmation**: Upon successful export, a confirmation message is printed to the standard output.

## 🚀 Usage Protocols

Execute the script from a terminal within its directory. No command-line arguments are required.

```sh
python GitExporttoyaml.py
```

The script operates on predefined paths within the code. To change the target scan directory or the output file location, the `base_path` and `export_file` variables must be modified directly in the script source.
