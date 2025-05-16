import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

KEYWORDS = ["crypto", "bit", "bitcoin", "coin", "ethereum", "blockchain", "t.me"]
ARCHIVE_URL = "https://pastebin.com/archive"
RAW_URL = "https://pastebin.com/raw/"
OUTPUT_FILE = "keyword_matches.jsonl"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_latest_paste_ids():
    response = requests.get(ARCHIVE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("table.maintable a")
    paste_ids = [link["href"].strip("/") for link in links if link["href"].startswith("/")]
    return paste_ids[:30]

def fetch_paste_content(paste_id):
    url = RAW_URL + paste_id
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    return ""

def check_keywords(content):
    found = [kw for kw in KEYWORDS if kw.lower() in content.lower()]
    return found

def save_to_file(matches):
    with open(OUTPUT_FILE, "a") as f:
        f.write(json.dumps(matches) + "\n")

def main():
    paste_ids = get_latest_paste_ids()
    for pid in paste_ids:
        content = fetch_paste_content(pid)
        if not content:
            continue

        keywords_found = check_keywords(content)
        if keywords_found:
            data = {
                "source": "pastebin",
                "context": f"Found crypto-related content in Pastebin paste ID {pid}",
                "paste_id": pid,
                "url": f"https://pastebin.com/raw/{pid}",
                "discovered_at": datetime.utcnow().isoformat() + "Z",
                "keywords_found": keywords_found,
                "status": "pending"
            }
            save_to_file(data)
            print(f"[+] Match found: {pid}")
        else:
            print(f"[-] No match: {pid}")

        time.sleep(2)  # Rate limit

if __name__ == "__main__":
    main()
