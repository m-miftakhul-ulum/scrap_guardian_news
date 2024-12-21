# The Guardian Sports News Scraper and Data Manager

This project is a web scraper for extracting sports news from **The Guardian's UK Sports** section. It processes the data, stores it in an SQLite database, and provides options to export the data in various formats (Excel, CSV, or JSON).

## Features

- **Scrape Sports News**: Extract titles, URLs, and article content from The Guardian's UK Sports section.
- **Data Storage**: Save scraped data to an SQLite database using the `dataset` library.
- **Flexible Data Export**: Export stored data to Excel, CSV, or JSON formats.
- **Query Support**: Run SQL queries on the stored data to analyze or retrieve specific information.

## Prerequisites

1. **Python 3.7+**  
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have an SQLite-compatible environment (SQLite is typically included with Python).

## Code Overview

1. **Scraping News Content**:  
   - `get_url()` scrapes article titles and links.  
   - `get_content(url)` retrieves the full article content from the link.

2. **Storing Data**:  
   - The scraped data is stored in an SQLite database (`mydatabase.db`) in the table `news_tabel`.
   - The `save()` function maps scraped data to a `News` model and inserts it into the database.

3. **Exporting Data**:  
   - The `save_choice()` function allows the user to export data in **Excel**, **CSV**, or **JSON** formats.

4. **Querying Data**:  
   - The `query()` function executes custom SQL queries on the database.

5. **CLI Options**:  
   - Choose actions like **scraping new data**, **saving data to files**, or **running custom queries** via a simple command-line interface.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/guardian-sports-scraper.git
   cd guardian-sports-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python script.py
   ```

## Usage

1. **Scrape Data**:
   - Run the script and choose option `1` to scrape sports articles from The Guardian.

2. **Save Data to Files**:
   - After scraping, choose option `2` to export data to your preferred format.

3. **Run Queries**:
   - Choose option `3` to input and execute a custom SQL query on the stored data.

## Example Workflow

1. Scrape data from The Guardian:
   ```text
   1. Get Data
   2. Save Data
   3. Show Data
   pilih nomor: 1
   ```
2. Save the scraped data to Excel:
   ```text
   Pilihan penyimpanan (1. Excel, 2. CSV, 3. JSON): 1
   Data berhasil disimpan ke file data.xlsx
   ```
3. Query stored data:
   ```text
   Masukkan query: SELECT * FROM news_tabel WHERE title LIKE '%football%'
   ```

## Dependencies

- `curl-cffi`: Makes HTTP requests with browser impersonation.
- `beautifulsoup4`: Parses HTML to extract required content.
- `dataset`: Simplifies database operations for storing and retrieving data.
- `pandas`: Manages and exports data to different formats.

## Data Example

Sample structure of scraped and exported data:

| Title                   | URL                                  | Content                |
|-------------------------|--------------------------------------|------------------------|
| Example News Title      | https://www.theguardian.com/abc123  | Full article content.  |

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

- **Respect Website Policies**: Scraping content from The Guardian should adhere to their terms of service.
- **Educational Use**: This project is intended for educational purposes only. The author is not responsible for any misuse.