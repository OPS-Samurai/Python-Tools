# 🏗️ Web-Crawler Architecture
> An interactive command-line tool designed to extract article data from websites, filter it based on user-defined criteria, and generate a live HTML report.

## 📂 Modules
| Module | Focus & Purpose | Status |
| :--- | :--- | :--- |
| [📁 crawler.py](./crawler.py) | Main executable script providing the user interface for initiating and configuring the crawl. | Active |
| [📁 ArticleFetcher.py](./ArticleFetcher.py) | Core class responsible for handling HTTP requests, parsing HTML, and extracting article data page by page. | Active |
| [📁 CrawledArticle.py](./CrawledArticle.py) | Data structure (dataclass) for storing the extracted information of a single article. | Stable |

---

# 📝 crawler.py
An interactive web crawler for extracting article information from websites. It prompts the user for a target URL, filters, and CSS selectors, then generates a live HTML report with the findings.

## 🛠️ Prerequisites
- Python 3.x
- `ArticleFetcher` class from `ArticleFetcher.py`
- Standard libraries: `os`, `json`, `webbrowser`, `winsound`, `datetime`

## ⚙️ Technical Details
The script operates through a `main()` function which orchestrates the crawling process.

- **User Input**: It interactively prompts the user for:
    - The target URL.
    - A keyword to filter results.
    - A comma-separated list of blacklist terms to exclude results.
    - Confirmation or modification of the default CSS selectors used for data extraction.

- **Data Fetching**: It instantiates `ArticleFetcher` and iterates through the articles it yields from the target site.

- **Filtering**:
    - **Keyword Filter**: If a keyword is provided, only articles whose title or brand contains the keyword are included.
    - **Blacklist Filter**: Articles containing any of the blacklisted terms are excluded.

- **Live Reporting**:
    - The `generate_html_report()` function creates a formatted HTML file from the results.
    - The report is updated every 5 articles found.
    - The script automatically opens the report in a web browser on the first update and upon completion.

- **Completion**: A final report is generated when the crawl finishes or is interrupted. A system beep signals the end of the process.

## 🚀 Usage (Examples)
Run the script from the command line. The script will guide you through the required inputs.

```bash
python crawler.py
```

**Example Interaction:**
```
--- JARVIS CRAWLER v4.5 (MANUAL OVERRIDE ENABLED) ---
Ziel-URL (Enter für Mein-Deal.com): https://www.example-shop.com/deals
Harter Filter (Keyword - Enter für alles): laptop
Blacklist (Begriffe mit Komma trennen - z.B. 'Halterung, Kabel'): bag, case

--- SELEKTOREN KONFIGURATION ---
Aktuelle Selektoren: {'container': 'article', 'title': 'h2', 'next_btn': 'a.next', 'image': 'img'}
Selektoren anpassen? (j/n): n

[*] Mission gestartet. Filter: laptop | Blacklist: 2 Begriffe
```

---

# 📝 ArticleFetcher.py
A class designed to fetch and parse articles from a web page, handling pagination to scrape multiple pages.

## 🛠️ Prerequisites
- Python 3.x
- `requests`
- `beautifulsoup4`
- `CrawledArticle` class from `CrawledArticle.py`

## ⚙️ Technical Details
### `ArticleFetcher` Class
- **`log_error(message)`**: Writes error messages with a timestamp to a local file named `crawler_errors.log`.
- **`fetch(url, selectors)`**: A generator function that performs the core crawling logic.
    - It sends an HTTP GET request to the given `url` with a standard `User-Agent` header.
    - It paginates by finding the "next" button using the provided `next_btn` CSS selector and following its `href` attribute.
    - To avoid rate-limiting, it pauses for 1.5 seconds between requests and for 3 minutes after every 100 pages.
    - It uses `BeautifulSoup` to parse the HTML and extracts article data based on the provided CSS selectors for the container, title, and image.
    - It attempts to find common selectors for price (`.price`, `.deal-price`) and brand (`.brand`, `.merchant`).
    - For each article found, it yields a `CrawledArticle` object containing the extracted data.
    - The process stops if no more articles are found or the "next" button is absent.

## 🚀 Usage (Examples)
Instantiate the class and loop through the `fetch` method to retrieve articles.

```python
from ArticleFetcher import ArticleFetcher

fetcher = ArticleFetcher()
target_url = "https://www.example-shop.com/deals"
css_selectors = {
    "container": ".product-card",
    "title": ".product-title",
    "next_btn": "a.pagination-next",
    "image": "img.product-image"
}

for article in fetcher.fetch(target_url, css_selectors):
    print(f"Found: {article.title} - {article.price}")

```

---

# 📝 CrawledArticle.py
A simple data class to provide a structured representation of a scraped article.

## 🛠️ Prerequisites
- Python 3.7+ (`dataclasses` module)

## ⚙️ Technical Details
The `@dataclass` decorator automatically generates methods like `__init__` and `__repr__`.

- **Attributes**:
    - `title` (str): The title of the article.
    - `brand` (str): The brand or manufacturer.
    - `price` (str): The price of the article.
    - `image` (str): The URL of the article's image.
    - `url` (str): The direct URL to the article page.

- **Methods**:
    - **`to_dict()`**: Returns a dictionary representation of the article's data.

## 🚀 Usage (Examples)
Create an instance to store article data.

```python
from CrawledArticle import CrawledArticle

# Create an instance
article = CrawledArticle(
    title="Example Laptop",
    brand="TechBrand",
    price="$999.99",
    image="https://example.com/image.jpg",
    url="https://example.com/product/123"
)

# Access data
print(article.title)

# Convert to dictionary
article_dict = article.to_dict()
print(article_dict)
```
