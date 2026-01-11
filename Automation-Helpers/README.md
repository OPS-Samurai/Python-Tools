# Automation-Helpers Module

## Overview
GitExporttoyaml.py is a Python script designed to extract and export system configuration information from a Git repository. This script provides valuable insights into the current state of your repositories, including branch names, remote URLs, and more.

## Usage
To use this script, simply run it from the command line or within your favorite IDE. The script will scan the specified directory (default: `C:\\Git`) for all subdirectories that are Git repositories. For each repository found, it will extract the current branch name and remote URL, then write this information to a YAML file.

## Features
* Scans a specified directory for Git repositories
* Extracts branch names and remote URLs from each repository
* Writes system configuration information to a YAML file

## System Requirements
* Python 3.8 or later
* Git installed on the system (for repository scanning)

## Output File
The script will generate an output file named `OPS-Systems/system_profile.yaml` in the specified directory (`C:\\Git`). This file contains the extracted system configuration information in YAML format.

## History
This script was written to help streamline system administration tasks and provide valuable insights into Git repository configurations. Future updates may include additional features or improvements based on user feedback.

---
> All systems are managed under ISO/IEC 26514 compliant documentation standards via Local AI.
