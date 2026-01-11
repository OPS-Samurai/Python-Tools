# 💻 GitExporttoyaml.py Control Module

## 🛠️ Prerequisites

The module requires the following Python libraries to be available in the execution environment:
*   **os**: For interacting with the operating system, primarily for path manipulation and directory listing.
*   **yaml**: For serializing the collected data into the YAML format.
*   **subprocess**: To execute external Git commands for retrieving repository information.
*   **datetime**: To timestamp the data export.

## ⚙️ Technical Details

The script is designed to catalog Git repositories within a predefined base directory (`C:\Git`).

Its core function is to generate a `system_profile.yaml` file, which acts as a manifest of all located repositories. The process involves:
1.  **Initialization**: A primary dictionary, `manifest`, is created. It is pre-populated with static metadata, including a system identity, the export timestamp, and details about the target environment.
2.  **Repository Scanning**: The script iterates through each item in the `C:\Git` directory.
3.  **Git Information Retrieval**: For each sub-directory, it executes `git` commands via `subprocess` to determine the current branch and the "origin" remote URL. If a directory is not a Git repository, the branch is listed as "unknown" and the remote as "none".
4.  **Data Aggregation**: The name, full path, remote URL, and active branch of each repository are appended to the `repositories` list within the `manifest`.
5.  **YAML Export**: The completed `manifest` dictionary is written to `C:\Git\OPS-Systems\system_profile.yaml`, overwriting any existing file.

## 🚀 Usage Protocols

Execute the Python script directly from a compatible environment. No command-line arguments are required. The script operates on a hardcoded base path and output file location. Upon successful execution, it will print a confirmation message to the console indicating the export path.
