# 💻 ArticleFetcher Control Module
## 🛠️ Prerequisites
- `time`
- `requests`
- `bs4` (BeautifulSoup)
- `urllib.parse`
- `CrawledArticle` data class
- `datetime`

## ⚙️ Technical Details
The `ArticleFetcher` class is designed to scrape article data from web pages. It systematically navigates through paginated sites, extracts specified data points for each article, and handles potential errors during the process.

- **Error Logging**: The `log_error` method records any exceptions encountered during fetching into a `crawler_errors.log` file, timestamping each entry for debugging purposes.
- **Data Fetching**: The `fetch` method is a generator that iterates through website pages.
    - It sends HTTP GET requests with a `User-Agent` header to mimic a standard web browser.
    - To prevent server overload, it pauses for 1.5 seconds between requests and implements a longer 3-minute pause every 100 pages.
    - It uses `BeautifulSoup` to parse the HTML content and CSS selectors provided in a `selectors` dictionary to find the article container, title, price, brand, image, and link.
    - For each article found, it yields a `CrawledArticle` object populated with the extracted data.
    - It identifies the "next page" button using a selector to continue the crawling process until no more pages are found.
- **URL Handling**: It uses `urljoin` to correctly construct absolute URLs from relative paths found in links and image sources.

## 🚀 Usage Protocols
The `ArticleFetcher` is not a standalone script. It must be imported and utilized by a primary control script.

1.  Instantiate the class: `fetcher = ArticleFetcher()`
2.  Call the `fetch` method, providing a starting URL and a dictionary of CSS selectors.
3.  Iterate over the returned generator to process each `CrawledArticle` object as it is yielded.

*Example Selectors Dictionary:*
```python
selectors = {
    'container': 'article',
    'title': 'h2.product-title a',
    'image': 'img.product-image',
    'next_btn': 'a.pagination-next'
}
```

---

# 💻 CrawledArticle Control Module
## 🛠️ Prerequisites
- `dataclasses` module

## ⚙️ Technical Details
`CrawledArticle` is a data class that serves as a structured container for information scraped from a website. It provides a standardized format for holding article details, ensuring data consistency throughout the crawling and reporting process.

The class defines the following attributes:
- `title` (str): The name or title of the article.
- `brand` (str): The brand or manufacturer of the article.
- `price` (str): The price of the article.
- `image` (str): The URL of the article's image.
- `url` (str): The direct URL to the article's page.

It also includes a `to_dict` method, which converts an instance of the class into a key-value dictionary format.

## 🚀 Usage Protocols
This class is primarily used as a data structure. An instance of `CrawledArticle` is created to represent a single scraped item. It is instantiated by providing values for the title, brand, price, image, and URL.

*Example Instantiation:*
```python
article = CrawledArticle(
    title="Product Example",
    brand="ExampleBrand",
    price="$99.99",
    image="https://example.com/image.jpg",
    url="https://example.com/product"
)
```

---

# 💻 Web Crawler Control Module
## 🛠️ Prerequisites
- `os`
- `json`
- `webbrowser`
- `winsound`
- `datetime`
- `ArticleFetcher` class

## ⚙️ Technical Details
This script provides an interactive command-line interface for crawling websites to extract article data. It orchestrates the fetching, filtering, and reporting of results.

- **HTML Report Generation**: The `generate_html_report` function creates a self-contained HTML file to display the crawled data.
    - The report is styled with a dark theme and includes columns for the product image, brand, title (with a hyperlink), and price.
    - It features a meta refresh tag to automatically reload the page every 60 seconds, allowing for live monitoring of results.
    - The generated file is named based on the filter keyword used for the session.
- **Main Execution Logic**: The `main` function controls the user interaction and crawling process.
    - It prompts the user to input a target URL, an optional keyword filter, and an optional comma-separated blacklist of terms.
    - It allows the user to review and override the default CSS selectors (`container`, `title`, `next_btn`, `image`) for the target site.
    - It instantiates the `ArticleFetcher` and begins the crawl.
    - For each article found, it checks if it matches the keyword filter and is not present in the blacklist.
    - Matching articles are added to a results list, and the HTML report is updated every 5 articles.
    - The script automatically opens the report file in the default web browser on the first update.
    - The process can be terminated manually by the user with `Ctrl+C`.
- **User Feedback**: The script provides real-time feedback in the console, indicating the current page being scanned and notifying when new articles are found. Upon successful completion, it plays a sound notification.

## 🚀 Usage Protocols
The script is designed to be executed directly from a terminal.

1.  Run the script: `python crawler.py`
2.  Follow the interactive prompts:
    - **Target-URL**: Enter the full URL of the website to crawl. Pressing Enter defaults to "https://www.mein-deal.com".
    - **Filter Keyword**: Enter a keyword to only save articles matching this term. Pressing Enter disables the filter.
    - **Blacklist**: Enter comma-separated terms to exclude from results.
    - **Selector Configuration**: Acknowledge the default CSS selectors or choose to customize them for the target website.
3.  The crawl begins, and a live HTML report will open in a web browser once the first set of results is found.
4.  The process concludes when the crawler can no longer find a "next page" button or is manually stopped. A final report is generated.
