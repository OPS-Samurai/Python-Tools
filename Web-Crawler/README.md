## **ISO Documentation: Interactive Web Crawler v4.5**

#### **1. Overview**

This document outlines the functionality and operation of the Interactive Web Crawler, a Python-based tool designed for targeted data extraction from websites.

The system is architected into three distinct modules:

*   **`crawler.py`**: The primary execution script and user interface. It manages user input, orchestrates the crawling process, applies filtering logic, and generates the final output report.
*   **`ArticleFetcher.py`**: The core crawling engine. This module is responsible for handling HTTP requests, parsing HTML content using BeautifulSoup, extracting data based on CSS selectors, and navigating through paginated content. It includes error logging and mechanisms to prevent rapid, excessive requests.
*   **`CrawledArticle.py`**: A `dataclass`-based data structure that defines the schema for a single extracted article. It standardizes the data object with fields for `title`, `brand`, `price`, `image`, and `url`.

The tool's primary function is to allow a user to interactively configure and launch a web crawl on a target website. It systematically navigates through pages, extracts specified article-like information (e.g., products, deals, news), filters the results based on a keyword and a blacklist, and presents the findings in a live-updating, formatted HTML report that can be monitored in a web browser.

#### **2. Prerequisites**

To operate the crawler, the following software components are required:

*   **Python 3.6** or higher.
*   **Required Python Libraries:**
    *   `requests`: For executing HTTP requests to fetch web page content.
    *   `beautifulsoup4`: For parsing HTML and extracting data elements.
    *   `winsound`: (Standard library, Windows-specific) Used for audio notifications upon task completion.

These dependencies can be installed using the Python package installer, pip:
```bash
pip install requests beautifulsoup4
```

#### **3. Usage**

##### **3.1. Execution**

The application is launched by running the main script from a terminal or command prompt:

```bash
python Web-Crawler/crawler.py
```

##### **3.2. Interactive Configuration**

Upon execution, the script prompts the user for several configuration parameters to define the scope and target of the crawl:

1.  **Target URL**: The initial URL from which the crawl will begin. If left blank, it defaults to `https://www.mein-deal.com`.
2.  **Keyword Filter**: A case-insensitive keyword used to filter results. Only articles containing this keyword in their title or brand will be collected. If left blank, all articles are considered.
3.  **Blacklist**: A comma-separated list of case-insensitive terms. Any article whose title or brand contains one of these terms will be excluded.
4.  **Selector Configuration**: The user is prompted to confirm or override the default CSS selectors used for data extraction. This allows the crawler to be adapted to different website structures.
    *   **`container`**: The selector for the parent element that encloses all data for a single article (Default: `article`).
    *   **`title`**: The selector for the element containing the article's title (Default: `h2`).
    *   **`next_btn`**: The selector for the anchor (`<a>`) tag that links to the next page of results (Default: `a.next`).
    *   **`image`**: The selector for the image (`<img>`) tag associated with the article (Default: `img`).

##### **3.3. Process Monitoring**

*   The console displays real-time progress, indicating the current page URL being scanned.
*   As matching articles are found and filtered, a confirmation message is printed.
*   The system generates and updates an HTML report (`Live_Report_*.html`) for every 5 articles found.
*   After the first 5 articles are found, the HTML report is automatically opened in the system's default web browser. This report is configured to auto-refresh every 60 seconds, providing a live dashboard of the crawl's progress.
*   The process can be terminated gracefully at any time by pressing `CTRL+C`.

##### **3.4. Outputs**

1.  **HTML Report**: A file named `Live_Report_<Keyword>.html` (or `Live_Report_All.html` if no keyword is used) is created in the script's directory. This file contains a formatted table of all collected articles.
2.  **Error Log**: If any HTTP or parsing errors occur during the crawl, they are logged with a timestamp in `crawler_errors.log`.
3.  **Completion Notification**: Upon successful completion of the crawl, a two-tone beep is played (Windows systems only) to alert the user.
