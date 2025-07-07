# tests/test_brochure_builder.py

import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brochure.brochure_builder import get_links, get_all_details, create_brochure

def test_get_links():
    url = "https://edwarddonner.com"
    links = get_links(url)
    
    print("\n🔗 Extracted Links JSON:")
    print(links)
    
    assert isinstance(links, dict), "Result should be a dictionary"
    assert "links" in links, "Missing 'links' key in response"
    assert isinstance(links["links"], list), "'links' should be a list"


def test_get_all_details():
    url = "https://edwarddonner.com"
    details = get_all_details(url)

    print("\n📄 Extracted Details (first 500 characters):")
    print(details[:500])
    
    assert isinstance(details, str), "Content should be a string"
    assert "Landing page" in details, "Expected 'Landing page' section"


def test_create_brochure():
    company_name = "Edward Donner"
    url = "https://edwarddonner.com"
    
    try:
        create_brochure(company_name, url)
        print("\n✅ Brochure displayed successfully")
    except Exception as e:
        assert False, f"Brochure generation failed with error: {e}"


if __name__ == "__main__":
    
    test_create_brochure()
