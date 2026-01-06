import os
import yaml
import subprocess
from datetime import datetime

def get_git_info(path):
    try:
        branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=path).decode().strip()
        remote = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=path).decode().strip()
        return {"branch": branch, "remote": remote}
    except:
        return {"branch": "unknown", "remote": "none"}

# System-Kontext definieren
base_path = "C:\\Git"
manifest = {
    "system_identity": "Jarvis-Core / OPS-Samurai",
    "export_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "environment": {
        "workspace_root": base_path,
        "powershell_profile": "C:\\Git\\OPS-Systems\\Windows-Core\\profile.ps1",
        "os_compatibility": ["PowerShell 5.1", "PowerShell 7.5.4"]
    },
    "repositories": []
}

# Repositories scannen
if os.path.exists(base_path):
    for folder in os.listdir(base_path):
        repo_path = os.path.join(base_path, folder)
        if os.path.isdir(repo_path):
            git_info = get_git_info(repo_path)
            manifest["repositories"].append({
                "name": folder,
                "path": repo_path,
                "remote": git_info["remote"],
                "active_branch": git_info["branch"]
            })

# Exportieren
export_file = os.path.join(base_path, "OPS-Systems", "system_profile.yaml")
with open(export_file, 'w', encoding='utf-8') as f:
    yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)

print(f"✅ System-DNA erfolgreich nach {export_file} exportiert.")