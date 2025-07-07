# brochure/scraping.py

import requests
from bs4 import BeautifulSoup

# Custom headers for websites that block default user agents
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

class Website:
    """
    Represents a scraped website with useful text and links.
    """

    def __init__(self, url: str):
        self.url = url
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching URL: {e}")

        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')

        # Extract title
        self.title = soup.title.string.strip() if soup.title else "No title found"

        # Clean up body text
        if soup.body:
            for tag in soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

        # Extract all links
        raw_links = [link.get("href") for link in soup.find_all("a")]
        self.links = [link for link in raw_links if link]

    def get_contents(self) -> str:
        """
        Returns a formatted version of the scraped webpage contents.
        """
        return f"Webpage Title:\n{self.title}\n\nWebpage Contents:\n{self.text}\n"

    def get_links(self) -> list:
        return self.links
