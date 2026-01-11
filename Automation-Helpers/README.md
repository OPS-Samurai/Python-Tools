# Git Repository YAML Exporter

This script scans a specified base directory for Git repositories and exports their details into a YAML file. It captures the repository's name, path, remote URL, and the currently active branch.

## Features

-   **System Scan:** Scans a predefined root folder for Git repositories.
-   **Git Integration:** Extracts the current branch and remote URL for each repository.
-   **YAML Export:** Gathers all repository information into a structured YAML file.
-   **System Context:** Includes metadata about the system, such as an identity, export timestamp, and environment details.

## How It Works

1.  **Initialization:** A main dictionary `manifest` is created to hold the system and repository information. It's pre-populated with system identity, the current timestamp, and environment details.
2.  **Repository Scan:** The script iterates through all subdirectories in the configured `base_path`.
3.  **Git Info Extraction:** For each subdirectory, it runs `git` commands (`git branch --show-current` and `git remote get-url origin`) to get the active branch and the remote origin URL. If a directory is not a Git repository or these commands fail, it defaults to "unknown" and "none".
4.  **Manifest Population:** The details for each discovered repository are added to the `repositories` list within the `manifest`.
5.  **YAML Export:** The final `manifest` dictionary is written to a `system_profile.yaml` file in a specified location.

## Configuration

-   **Base Path:** To change the root directory for the repository scan, modify the `base_path` variable.

    ```python
    base_path = "C:\\Your\\Path\\To\\Git\\Repositories"
    ```

-   **Output File:** To change the destination of the YAML export, modify the `export_file` variable.

    ```python
    export_file = os.path.join(base_path, "your_folder", "your_file.yaml")
    ```

## Dependencies

The script requires the `PyYAML` library to be installed.

```sh
pip install pyyaml
```

## Usage

Execute the script from your terminal:

```sh
python GitExporttoyaml.py
```

Upon successful execution, it will print a confirmation message:

```
✅ System-DNA erfolgreich nach C:\Git\OPS-Systems\system_profile.yaml exportiert.
```

## Output Example (`system_profile.yaml`)

The generated output file will look similar to this:

```yaml
system_identity: Jarvis-Core / OPS-Samurai
export_date: '2023-10-27 10:30:00'
environment:
  workspace_root: C:\Git
  powershell_profile: C:\Git\OPS-Systems\Windows-Core\profile.ps1
  os_compatibility:
  - PowerShell 5.1
  - PowerShell 7.5.4
repositories:
- name: MyProject1
  path: C:\Git\MyProject1
  remote: https://github.com/user/myproject1.git
  active_branch: main
- name: AnotherRepo
  path: C:\Git\AnotherRepo
  remote: https://dev.azure.com/org/anotherrepo.git
  active_branch: develop
- name: NotAGitRepo
  path: C:\Git\NotAGitRepo
  remote: none
  active_branch: unknown
```

---
> All systems are managed under ISO/IEC 26514 compliant documentation standards.
