# 💻 ArticleFetcher Control Module
## 🛠️ Prerequisites
- `time`: For implementing delays between requests.
- `requests`: For making HTTP requests to fetch web page content.
- `BeautifulSoup` (from bs4): For parsing HTML documents.
- `urllib.parse.urljoin`: For constructing absolute URLs from relative paths.
- `CrawledArticle`: Local data structure for storing fetched article data.
- `datetime`: For timestamping error logs.

## ⚙️ Technical Details
The `ArticleFetcher` class is designed to scrape articles from a website with pagination. It simulates a browser user-agent to avoid request blocks. The core functionality is within the `fetch` generator method, which navigates from one page to the next using a provided CSS selector for the "next" button.

For each page, it extracts article containers and then parses individual data points (title, price, brand, URL, image) based on a dictionary of CSS selectors. To prevent overwhelming the target server, it incorporates a 1.5-second delay between requests and a 3-minute pause after every 100 pages. Errors during fetching are caught and logged to `crawler_errors.log` with a timestamp via the `log_error` method.

## 🚀 Usage Protocols
Instantiate the `ArticleFetcher` class. Call the `fetch(url, selectors)` method, providing the initial target URL and a dictionary of CSS selectors. The selectors dictionary must define keys for `container`, `title`, `image`, and `next_btn`. The method yields `CrawledArticle` objects as they are found.

***

# 💻 CrawledArticle Control Module
## 🛠️ Prerequisites
- `dataclasses`: Required for the `@dataclass` decorator.

## ⚙️ Technical Details
`CrawledArticle` is a data class that serves as a structured container for information scraped from a website. It defines five string fields: `title`, `brand`, `price`, `image`, and `url`. The module also includes a `to_dict` method, which converts an instance of the class into a standard dictionary format.

## 🚀 Usage Protocols
Import the `CrawledArticle` class and create instances to hold the data for each scraped article. This ensures data consistency and provides a clean, object-oriented way to pass article information between different modules of the system.

***

# 💻 Crawler Control Module
## 🛠️ Prerequisites
- `os`, `webbrowser`, `winsound`: For interacting with the operating system (opening files, playing sounds).
- `json`: For data serialization (though not directly used in the visible code, it's a standard related module).
- `datetime`: For timestamping the generated HTML report.
- `ArticleFetcher`: The local module for the core crawling logic.

## ⚙️ Technical Details
This script serves as the main interactive entry point for the web crawler. It prompts the user for a target URL, an optional filtering keyword, a comma-separated blacklist, and allows for manual override of the default CSS selectors.

The `main` function orchestrates the process:
1.  It instantiates the `ArticleFetcher`.
2.  It iterates through the articles yielded by the fetcher.
3.  It applies the user-defined keyword filter and blacklist to the article's title and brand.
4.  Matching articles are appended to a results list.
5.  The `generate_html_report` function is called periodically (every 5 results) and at the end of the crawl to create a local HTML file. This file is automatically opened in the default web browser on the first update to provide a live dashboard.
The script includes `try...except KeyboardInterrupt` for graceful shutdown by the user. A system sound indicates the completion of the task.

## 🚀 Usage Protocols
Execute the script from a command-line interface. Follow the interactive prompts to define the crawl target, filters, and selectors. The system will automatically launch the crawl and open the live HTML report in a web browser. The process runs until all pages are scraped or it is manually terminated by the operator.
