Error executing tool write_file: Tool "write_file" not found in registry. Tools must use the exact names that are registered. Did you mean one of: "read_file", "write_todos", "glob"?
Error executing tool run_shell_command: Tool "run_shell_command" not found in registry. Tools must use the exact names that are registered. Did you mean one of: "search_file_content", "read_file", "save_memory"?
I am unable to directly create or write files to the file system with the available tools. However, I have generated the content for the `README.md` file based on your requirements. Please create the `Web-Crawler/README.md` file and paste the following content into it:

```markdown
# Web-Crawler Automation
> This module provides an interactive web crawler designed to extract article-like content from websites, offering features for filtering, blacklisting, and generating live HTML reports.

## Included Scripts
| File | Description |
| :--- | :--- |
| ArticleFetcher.py | Handles the core logic for fetching web pages, parsing HTML content using user-defined selectors, and extracting article data. It supports pagination and includes error logging. |
| CrawledArticle.py | Defines a data structure (dataclass) to hold the extracted information for a single crawled article, including title, brand, price, image URL, and article URL. |
| crawler.py | The main executable script that orchestrates the web crawling process. It prompts the user for a target URL, keywords, blacklisted terms, and custom CSS selectors. It then uses `ArticleFetcher` to gather data and generates a live-updating HTML report of the findings. |

## Usage
To run the web crawler, execute the `crawler.py` script. The script will guide you through the configuration steps, including specifying the target URL, keywords, blacklist terms, and optional CSS selectors.

```bash
python crawler.py
```

Upon execution, you will be prompted for the following:
1.  **Target URL**: The starting URL for the crawl. (Default: `https://www.mein-deal.com`)
2.  **Hard Filter (Keyword)**: An optional keyword to filter articles. Only articles containing this keyword in their title or brand will be included. (Leave empty for no keyword filter)
3.  **Blacklist**: A comma-separated list of terms. Articles containing any of these terms in their title or brand will be excluded.
4.  **Selectors Configuration**: Option to customize the CSS selectors used for identifying article containers, titles, next page buttons, and images. Default selectors are provided as a suggestion.

The script will then begin crawling, displaying progress in the console and generating an HTML report (`Live_Report_[Keyword].html`) that opens automatically in your web browser, updating live as new articles are found.

---
*Module Version: Automated Build (Jarvis ISO Protocol)*
```

---
> All systems are managed under ISO/IEC 26514 compliant documentation standards.
