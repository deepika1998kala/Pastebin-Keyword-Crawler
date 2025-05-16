# Pastebin Keyword Crawler
This Python script scrapes Pastebin's public archive for pastes containing specific keywords related to cryptocurrencies (e.g., "crypto", "bitcoin", "ethereum") or Telegram links (e.g., "t.me"). The relevant pastes are then stored in a structured format (JSON) in a file.

A Python script to crawl recent public pastes on Pastebin.com and search for specified keywords like `crypto`, `telegram`, `btc`, etc.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pastebin-keyword-crawler.git
   cd pastebin-keyword-crawler

2. Install dependencies:
pip install -r requirements.txt

3. Install Required Libraries:
pip install requests beautifulsoup4

## Command-Line Usage

1. Run the Script
To start scraping Pastebin and find pastes with the specified keywords, run the following command:
python pastebin_keyword_crawler.py
2. Output File
The script will create a keyword_matches.jsonl file in the same directory. This file will contain the details of all the pastes that match the keywords, in the following format:
Then, commit and push this file to the remote repository:
{
  "source": "pastebin",
  "context": "Found crypto-related content in Pastebin paste ID abc123",
  "paste_id": "abc123",
  "url": "https://pastebin.com/raw/abc123",
  "discovered_at": "2025-05-12T10:00:00Z",
  "keywords_found": ["crypto", "bitcoin"],
  "status": "pending"
}
3. Check the logs for progress
The script prints out a log of each paste it processes, showing whether a match was found or skipped.

Files
pastebin_keyword_crawler.py: The main script that performs the scraping and keyword matching.

requirements.txt: The list of required Python libraries.

keyword_matches.jsonl: The output file that stores the pastes containing the specified keywords.

##  Sample Output
[+] Found keyword 'crypto' in: https://pastebin.com/abc123
[+] Found keyword 'telegram' in: https://pastebin.com/xyz456
[+] No matches found on page 3

##  How It Works
The script scrapes recent public pastes from Pastebin.

It downloads the content of each paste.

Then it checks if any of the user-provided keywords are found.

Matching URLs are printed to the console.

## Screenshot (POC)

![Tool Screenshot](POC.png)


## Features
   1. Scrapes Pastebin’s public archive for pastes containing keywords related to:
   
      -> Crypto-related terms: "crypto", "bitcoin", "ethereum", "blockchain", etc.
      
      -> Telegram links: "t.me"
   
   2. Retrieves the latest 30 Paste IDs from Pastebin's archive.
   
   3. Fetches the raw content of each paste and checks for keyword matches.
   
   4. Stores matching pastes in a JSON Lines format (keyword_matches.jsonl).
   
   5. Logs the paste check status (e.g., match found, no match, or errors).
   
   6. Implements rate-limiting with time.sleep() to avoid getting blocked.

🧑‍💻 Author
Deepika Kala
