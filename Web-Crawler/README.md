# 💻 ArticleFetcher Control Module

## 🛠️ Prerequisites

This module requires the following libraries and classes to be available in the execution environment:
*   `time`: For pausing execution.
*   `requests`: For making HTTP requests.
*   `BeautifulSoup` (from `bs4`): For parsing HTML documents.
*   `urljoin` (from `urllib.parse`): For constructing absolute URLs.
*   `CrawledArticle`: Data class for storing fetched article details.
*   `datetime` (from `datetime`): For timestamping error logs.

## ⚙️ Technical Details

The `ArticleFetcher` class is designed to scrape paginated websites for article-like entries.

*   **`log_error(message)`**: This method logs any exceptions encountered during the fetching process to a local file named `crawler_errors.log`. Each log entry is timestamped.

*   **`fetch(url, selectors)`**: This is a generator method that navigates a target website.
    *   It sends HTTP GET requests with a standard `User-Agent` header to mimic a web browser.
    *   It iterates through pages by finding a "next page" link using a provided CSS selector (`selectors['next_btn']`).
    *   On each page, it extracts article containers based on `selectors['container']`.
    *   For each article, it extracts the title, price, brand, URL, and image using corresponding CSS selectors.
    *   It introduces a 1.5-second delay between requests to avoid overwhelming the server.
    *   A 3-minute pause is automatically triggered after every 100 pages crawled.
    *   It yields `CrawledArticle` objects for each successfully parsed article.

## 🚀 Usage Protocols

To utilize the module, first instantiate the `ArticleFetcher` class. Then, call the `fetch` method, providing the initial target URL and a dictionary of CSS selectors. The selectors dictionary must define keys for `container`, `title`, `next_btn`, and `image`. Iterate over the returned generator to process the `CrawledArticle` objects.

---

# 💻 CrawledArticle Control Module

## 🛠️ Prerequisites

This module requires the `dataclass` decorator from the `dataclasses` library.

## ⚙️ Technical Details

`CrawledArticle` is a data class serving as a structured container for information retrieved by the web crawler. It defines the following attributes:

*   `title` (str): The title of the article.
*   `brand` (str): The brand or manufacturer name.
*   `price` (str): The price of the article.
*   `image` (str): The URL of the article's image.
*   `url` (str): The direct URL to the article page.

It also includes a `to_dict()` method, which converts the object's attributes into a dictionary format.

## 🚀 Usage Protocols

Instantiate the `CrawledArticle` class by providing values for the title, brand, price, image, and URL. The instance can then be used to pass structured article data between different components of the system.

---

# 💻 Crawler Control Module

## 🛠️ Prerequisites

This module requires the following libraries and classes:
*   `os`: For path manipulation.
*   `json`: For data serialization (not actively used in the provided code but may be intended for future use).
*   `webbrowser`: For automatically opening the HTML report in the user's default browser.
*   `winsound`: For playing system sounds upon task completion.
*   `datetime`: For timestamping the generated report.
*   `ArticleFetcher`: The core class for fetching web content.

## ⚙️ Technical Details

This script provides an interactive command-line interface for extracting article data from websites.

*   **`generate_html_report(results, keyword)`**: This function takes a list of `CrawledArticle` objects and a keyword, then generates a self-contained HTML file. The report is styled with CSS for readability and includes a live-updating timestamp. The generated filename is based on the keyword (e.g., `Live_Report_All.html`).

*   **`main()`**: The primary execution function. It orchestrates the entire crawling process:
    1.  **User Input**: Prompts the user to enter a target URL, a filtering keyword, and a comma-separated list of blacklist terms.
    2.  **Selector Configuration**: Presents a default set of CSS selectors and allows the user to override them interactively.
    3.  **Data Extraction**: Initializes `ArticleFetcher` and iterates through the yielded articles.
    4.  **Filtering**: Applies the user-defined keyword and blacklist filters to the title and brand of each article.
    5.  **Live Reporting**: For every 5 matching articles found, it regenerates the HTML report and, on the first update, opens it in a web browser.
    6.  **Completion**: Once the crawl is complete or interrupted (`KeyboardInterrupt`), it generates a final report and notifies the user with a system beep.

## 🚀 Usage Protocols

Execute the script directly from a command line. The user will be guided through a series of prompts to configure the crawl target and parameters. The script runs until all pages are processed or the user manually terminates it (Ctrl+C). A live HTML report is created in the script's directory.
