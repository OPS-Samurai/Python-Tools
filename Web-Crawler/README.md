I will now create the `README.md` file in the `Web-Crawler` directory using a Python command to write the content, as a direct file writing tool is unavailable.
# Web Crawler

This is a simple, interactive web crawler designed to extract article-like data from websites. It allows users to specify a target URL, define CSS selectors for data extraction, and filter the results based on keywords and a blacklist. The crawler generates a live HTML report of the findings, which is automatically opened and refreshed in your web browser.

## Features

- **Interactive Setup**: Configure the crawl session directly from the command line, including target URL, content filters, and CSS selectors.
- **Keyword Filtering**: Only scrapes articles that contain a specific keyword in their title or brand.
- **Blacklist Filtering**: Excludes articles containing specified blacklist words.
- **Custom CSS Selectors**: Adapt the crawler to different website structures by defining your own CSS selectors for the article container, title, image, and pagination button.
- **Live HTML Reports**: Generates an HTML report that updates every 5 articles found. The report is automatically opened in a web browser for live monitoring.
- **Error Logging**: Logs any errors during the crawling process to `crawler_errors.log`.

## Requirements

The project relies on the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## How to Use

1.  **Run the script** from your terminal:
    ```bash
    python crawler.py
    ```

2.  **Enter the Target URL**: Provide the full URL of the website you want to crawl. You can press Enter to use the default (`https://www.mein-deal.com`).

3.  **Set a Keyword Filter**: Enter a keyword to filter the results. Only articles matching this keyword will be saved. Press Enter to crawl all articles.

4.  **Set a Blacklist**: Enter a comma-separated list of words to exclude from the results (e.g., `case, cable`). Press Enter to skip.

5.  **Configure CSS Selectors**: The script will prompt you to configure the CSS selectors needed to find the data on the page. You can either accept the defaults or provide your own selectors for:
    -   **Container**: The selector for the main element that contains each article.
    -   **Title**: The selector for the article's title.
    -   **Next-Button**: The selector for the link to the next page.
    -   **Image**: The selector for the article's main image.

6.  **Monitor the Crawl**: The script will start crawling the website and display its progress. An HTML report will be generated and opened in your browser. This report will automatically refresh as more articles are found.

7.  **View the Results**: Once the crawl is complete or is stopped manually (with `Ctrl+C`), a final report is saved, and a sound will notify you. The final report file will be named `Live_Report_<Keyword>.html` or `Live_Report_All.html`.

## File Descriptions

-   **`crawler.py`**: The main script that handles user interaction, manages the crawling process, and generates the HTML report.
-   **`ArticleFetcher.py`**: Contains the core logic for fetching web pages, parsing the HTML with BeautifulSoup, and extracting article data based on the provided selectors.
-   **`CrawledArticle.py`**: A simple `dataclass` that defines the structure for a scraped article (title, brand, price, image, url).
-   **`requirements.txt`**: A list of Python dependencies required for the project.

---
> All systems are managed under ISO/IEC 26514 compliant documentation standards.
