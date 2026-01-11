# 💻 ArticleFetcher Control Module
## 🛠️ Prerequisites
- `time`: For handling delays and pauses during crawling.
- `requests`: For making HTTP requests to fetch web page content.
- `bs4` (BeautifulSoup): For parsing HTML documents and extracting data.
- `urllib.parse`: For joining relative URLs to form absolute URLs.
- `CrawledArticle`: Local data class for storing scraped article information.
- `datetime`: For timestamping error logs.

## ⚙️ Technical Details
The `ArticleFetcher` class is designed to scrape articles from a paginated website.

- **Error Logging**: The `log_error` method records any exceptions encountered during the fetching process into a file named `crawler_errors.log`, complete with a timestamp.
- **Fetching Process**: The core logic resides in the `fetch` generator method. It sequentially navigates through pages using a "next button" selector.
  - It simulates a browser user agent (`Mozilla/5.0`) in the request headers.
  - To prevent overloading the server, it pauses for 1.5 seconds between requests and implements a 3-minute pause after every 100 pages accessed.
  - It uses `requests.get` with a 15-second timeout and checks for HTTP errors via `raise_for_status()`.
- **Data Extraction**: For each page, `BeautifulSoup` parses the HTML. The method then:
  - Selects article containers based on the provided `container` selector.
  - Extracts the title, price, brand, article URL, and image URL using corresponding CSS selectors. If a specific element like brand or price is not found, it assigns a default value of "N/A".
  - Yields a `CrawledArticle` object for each successfully parsed article.
- **Pagination**: The crawler continues to the next page by finding an element matching the `next_btn` selector and extracting its `href` attribute. The process stops if no "next" button is found or if no articles are found on the current page.

## 🚀 Usage Protocols
The `ArticleFetcher` is intended to be used by an orchestrator script. To use it, create an instance of the class. Then, call the `fetch(url, selectors)` method, providing the initial target URL and a dictionary of CSS selectors. Iterate over the returned generator to process each `CrawledArticle` object as it is scraped.

---

# 💻 CrawledArticle Control Module
## 🛠️ Prerequisites
- `dataclasses`: Standard Python module for creating structured data classes.

## ⚙️ Technical Details
`CrawledArticle` is a data class that serves as a standardized container for information scraped from a website. It defines the structure for a single article, ensuring data consistency. The class attributes are:
- `title` (str)
- `brand` (str)
- `price` (str)
- `image` (str)
- `url` (str)

It also includes a `to_dict()` method, which converts an instance of the class into a key-value dictionary format.

## 🚀 Usage Protocols
This class is not executed directly. It is imported and instantiated by other modules (`ArticleFetcher`, `crawler.py`) to hold the extracted data for each article. An instance is created by passing the title, brand, price, image, and URL as arguments during its initialization.

---

# 💻 Crawler Control Module
## 🛠️ Prerequisites
- `os`: For handling file paths.
- `webbrowser`: For automatically opening the HTML report in the user's default browser.
- `winsound`: For playing system sounds as notifications (Windows-specific).
- `datetime`: For timestamping the generated report.
- `ArticleFetcher`: Local module for performing the web scraping.

## ⚙️ Technical Details
This script is the main entry point for the web crawling application.

- **HTML Report Generation**: The `generate_html_report` function dynamically creates an HTML file from a list of `CrawledArticle` objects. The report is styled with CSS for readability and includes a meta refresh tag to reload every 60 seconds, providing a live view of the results.
- **Interactive Configuration**: The `main` function initiates an interactive command-line session to configure the crawl:
  - It prompts the user for a target URL, an optional filtering keyword, and an optional comma-separated blacklist of terms.
  - It presents a default set of CSS selectors and allows the user to override them if needed.
- **Crawling and Filtering**:
  - An `ArticleFetcher` instance is created to perform the scraping.
  - For each article found, the script combines the title and brand into a single string for text matching.
  - It first applies the hard keyword filter (if provided).
  - It then checks the article against the blacklist. An article is excluded if any blacklisted word is found in its text.
- **Live Monitoring**:
  - As results are collected, the script updates the HTML report every 5 articles.
  - On the first update (at 5 results), it automatically opens the report file in a web browser.
- **Completion**: The process can be terminated manually by the user (`KeyboardInterrupt`). Upon completion or interruption, a final report is generated, opened in the browser, and a notification sound is played.

## 🚀 Usage Protocols
Execute the script from the command line. Follow the interactive prompts to specify the target URL and filtering criteria. The crawler will then run, and a live HTML report will be opened in your web browser.
