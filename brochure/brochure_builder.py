# brochure/brochure_builder.py

import json
import re
import time
import logging
from brochure.scraping import Website
from brochure.prompts import (
    link_system_prompt,
    get_links_user_prompt,
    get_brochure_user_prompt,
    brochure_system_prompt as system_prompt
)
from brochure.llm import generate_response
from IPython.display import Markdown, display, update_display

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_links(url: str) -> dict:
    logger.info(f"Extracting relevant links from: {url}")
    website = Website(url)
    prompt = link_system_prompt + "\n" + get_links_user_prompt(website)
    
    response = generate_response(prompt)
    result = response.strip()

    if result.startswith("```"):
        result = re.sub(r"^```[a-zA-Z]*\n?", "", result)
        result = re.sub(r"\n?```$", "", result)

    try:
        parsed = json.loads(result)
        logger.info(f"Found {len(parsed.get('links', []))} useful links.")
        return parsed
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from model response:\n{result}")
        raise e


def get_all_details(url: str) -> str:
    logger.info(f"Fetching landing page and related sections from: {url}")
    result = "Landing page:\n"
    result += Website(url).get_contents()

    links = get_links(url)
    for link in links.get("links", []):
        link_type = link.get("type", "Section").title()
        link_url = link.get("url")
        logger.info(f"Scraping: {link_type} at {link_url}")
        result += f"\n\n{link_type}\n"
        result += Website(link_url).get_contents()

    return result


def create_brochure(company_name: str, url: str):
    logger.info(f"Generating brochure for: {company_name}")
    website = Website(url)
    full_prompt = system_prompt + "\n" + get_brochure_user_prompt(company_name, website)
    
    response = generate_response(full_prompt)
    result = response.strip()

    if result.startswith("```"):
        result = re.sub(r"^```[a-zA-Z]*\n?", "", result)
        result = re.sub(r"\n?```$", "", result)

    display(Markdown(result))


# brochure/brochure_builder.py (safe stream for CLI or notebook)

def stream_brochure(company_name: str, url: str, stream: bool = True) -> str:
    logger.info(f"Streaming brochure creation for: {company_name}")
    website = Website(url)
    full_prompt = system_prompt + "\n" + get_brochure_user_prompt(company_name, website)

    response = generate_response(full_prompt)
    result = response.strip()

    # Clean markdown wrapper
    if result.startswith("```"):
        result = re.sub(r"^```[a-zA-Z]*\n?", "", result)
        result = re.sub(r"\n?```$", "", result)

    if stream:
        try:
            from IPython.display import Markdown, display, update_display
            display_handle = display(Markdown(""), display_id=True)
            streamed = ""
            for line in result.split('\n'):
                streamed += line + '\n'
                update_display(Markdown(streamed), display_id=display_handle.display_id)
                time.sleep(0.05)
        except Exception:
            # Fallback to printing if not in notebook
            for line in result.split('\n'):
                print(line)
                time.sleep(0.03)

    return result  # Always return final markdown string
