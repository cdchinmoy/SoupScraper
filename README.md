## **MoneyControl News Scraper**

This is a Python-based web scraping project using **Beautiful Soup 4**, designed specifically to extract news articles from [Moneycontrol.com](https://www.moneycontrol.com/).


## **Requirements**
- Python 3.7+
- Dependencies:
  - `beautifulsoup4`
  - `requests`
  - `lxml`
  - `tqdm`
 

## **Directory Structure**
```
SoupScraper/
│
├── scraper.py            # Main scraper script
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── .gitignore            # Specifies files and directories to ignore in Git version control
└── output/               # Directory for scraped JSON/CSV files
```


## **Features**
- **Targeted Scraper**: Tailor-made to extract news titles and images from Moneycontrol's articles.
- **Beautiful Soup 4**: Uses the powerful and flexible Beautiful Soup library for parsing HTML.
- **JSON Export**: Automatically saves scraped data into a JSON file for easy integration.
- **Pagination Support**: Handles multiple pages of news with dynamic URL handling.


## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cdchinmoy/moneycontrol-scraper.git
   cd moneycontrol-scraper
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


## **Usage**

1. **Edit the Target URL**:  
   Modify the `src_url` variable in the script to set the target URL for scraping.

   ```python
   src_url = "https://www.moneycontrol.com/news/business/"
   ```

2. **Run the Scraper**:  
   Execute the script using the following command:
   ```bash
   python scraper.py
   ```

3. **Output**:  
   Scraped data will be saved as a JSON file named with the current date.

4. **Optional CSV Export**:  
   You can modify the script to save the output in CSV format if needed.



## **Example Output**
A sample JSON output from the scraper:
```json
{
  "1": [
    {
      "title": ["Stock Market Updates: Top Gainers and Losers"],
      "img_src": ["https://images.moneycontrol.com/market-updates.jpg"]
    },
    {
      "title": ["Business Trends to Watch in 2024"],
      "img_src": ["https://images.moneycontrol.com/trends-2024.jpg"]
    }
  ]
}
```

