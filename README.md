# 🔧 Python-Tools

### Executive Summary

This repository hosts a collection of Python scripts designed for various automation and security tasks. The tools encompass functionalities for exporting Git repository information, network scanning, and web crawling for article data extraction. All documentation adheres to ISO/IEC 26514 compliant standards.

### Installation/Setup

To utilize the scripts in this repository, the necessary Python dependencies must be installed. It is highly recommended to use a virtual environment.

1.  **Create and Activate Virtual Environment (Optional, but Recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On Linux/macOS:
    . venv/bin/activate
    ```

2.  **Install Dependencies:**

    Navigate into the respective subdirectory and install the listed dependencies. For the Web-Crawler:

    ```bash
    cd Web-Crawler
    pip install -r requirements.txt
    ```

    For `Automation-Helpers/GitExporttoyaml.py`, `PyYAML` might be required if not already globally installed:

    ```bash
    pip install PyYAML
    ```

### Usage

#### Automation-Helpers

*   `GitExporttoyaml.py`: Gathers detailed information (such as current branch and remote URL) from Git repositories and exports it structurally to a YAML file.

#### Network-Scanner

*   `netscan.py`: A lean, Python-based port scanner used to identify open TCP ports on a specified target host.

#### Web-Crawler

*   `ArticleFetcher.py`: A class responsible for fetching web page content and parsing specific data (z.B. Titel, Marke, Preis) using defined selectors.
*   `CrawledArticle.py`: Defines a `dataclass` for standardized storage of extracted article information such as title, brand, price, image URL, and article URL.
*   `crawler.py`: A comprehensive web crawler that interactively searches websites, extracts article information, and summarizes it in a generated HTML report.

### Inventory

| File                                | Description                                                                                                                                                                                                       |
| :---------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Automation-Helpers/GitExporttoyaml.py` | Collects Git repository information (branch, remote) and exports it to a YAML file.                                                                                                                                 |
| `Network-Scanner/netscan.py`        | Simple TCP Port Scanner (Python). Usage: `netscan.py <IP>`                                                                                                                                                          |
| `Web-Crawler/ArticleFetcher.py`     | Class for fetching web content and extracting articles. Includes error logging.                                                                                                                                     |
| `Web-Crawler/CrawledArticle.py`     | Dataclass to store crawled article data (title, brand, price, image, url).                                                                                                                                        |
| `Web-Crawler/crawler.py`            | Interactive web crawler for extracting articles from websites, generating HTML reports.                                                                                                                             |

### Ordnerstruktur

```
.
├── Automation-Helpers
│   ├── GitExporttoyaml.py
│   └── README.md
├── Network-Scanner
│   ├── netscan.py
│   └── README.md
├── Web-Crawler
│   ├── ArticleFetcher.py
│   ├── CrawledArticle.py
│   ├── crawler.py
│   ├── README.md
│   └── requirements.txt
├── .gitignore
├── GEMINI_TASK.txt
├── README.md
└── .git
```

---
All systems are managed under ISO/IEC 26514 compliant documentation standards.