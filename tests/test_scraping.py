# tests/test_scraping.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brochure.scraping import Website


if __name__ == "__main__":
    url = "https://edwarddonner.com"  # safer for scraping
    site = Website(url)
    print(site.get_contents())
    print(site.get_links())
