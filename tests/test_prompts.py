# tests/test_prompts.py

import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brochure.scraping import Website
from brochure.prompts import get_links_user_prompt, link_system_prompt

def test_get_links_user_prompt():
    url = "https://edwarddonner.com"  # or any other site you prefer
    website = Website(url)
    
    user_prompt = get_links_user_prompt(website)

    print("\n--- Link System Prompt ---\n")
    print(link_system_prompt)

    print("\n--- User Prompt ---\n")
    print(user_prompt)  # Only print first 1000 characters

    assert "https://" in user_prompt or "/" in user_prompt, "Prompt should contain link(s)"
    assert website.url in user_prompt, "Prompt should include the website URL"
    assert "Links" in user_prompt, "Prompt should mention Links"

if __name__ == "__main__":
    test_get_links_user_prompt()
