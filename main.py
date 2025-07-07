# main.py

import os
from brochure.brochure_builder import stream_brochure

def save_brochure_to_file(markdown_text: str, filename: str = "README.md"):
    # Ensure the 'results' folder exists
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    filepath = os.path.join(results_dir, filename)

    # Save the markdown text
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    print(f"\n✅ Brochure saved at: {filepath}")


if __name__ == "__main__":
    print("📄 Brochure Generator")
    company_name = input("Enter the company name: ").strip()
    url = input("Enter the company website URL: ").strip()

    print(f"\n⏳ Generating brochure for {company_name}...\n")
    markdown_text = stream_brochure(company_name, url)

    save_brochure_to_file(markdown_text)
