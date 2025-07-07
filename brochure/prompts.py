# brochure/prompts.py

import logging
from brochure.scraping import Website

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------- LINK FILTERING PROMPT ----------
link_system_prompt = (
    "You are provided with a list of links found on a webpage. "
    "You are able to decide which of the links would be most relevant to include in a brochure about the company, "
    "such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
    "You should respond in JSON as in this example:\n"
    "{\n"
    '    "links": [\n'
    '        {"type": "about page", "url": "https://full.url/goes/here/about"},\n'
    '        {"type": "careers page", "url": "https://another.full.url/careers"}\n'
    "    ]\n"
    "}"
)

def get_links_user_prompt(website: Website) -> str:
    """
    Generates the user prompt for link classification.

    Args:
        website (Website): The Website object with scraped links.

    Returns:
        str: A prompt to classify links for brochure use.
    """
    logger.info("Generating user prompt for link filtering...")
    user_prompt = (
        f"Here is the list of links on the website of {website.url} - "
        "please decide which of these are relevant web links for a brochure about the company, "
        "respond with the full https URL in JSON format. "
        "Do not include Terms of Service, Privacy, email links.\n\n"
        "Links (some might be relative links):\n"
        + "\n".join(website.links)
    )
    return user_prompt


# ---------- BROCHURE GENERATION PROMPT ----------
brochure_system_prompt = (
    "You are an assistant that analyzes the contents of several relevant pages from a company website "
    "and creates a short brochure about the company for prospective customers, investors and recruits. "
    "Respond in markdown. Include details of company culture, customers and careers/jobs if you have the information."
)

# Optional humorous version (commented)
# brochure_system_prompt = (
#     "You are an assistant that analyzes the contents of several relevant pages from a company website "
#     "and creates a short humorous, entertaining, jokey brochure about the company for prospective customers, investors and recruits. "
#     "Respond in markdown. Include details of company culture, customers and careers/jobs if you have the information."
# )

def get_brochure_user_prompt(company_name: str, website: Website) -> str:
    """
    Generates the user prompt to feed scraped text into the brochure-generation LLM prompt.

    Args:
        company_name (str): Name of the company.
        website (Website): Scraped website content.

    Returns:
        str: The user prompt including extracted website content.
    """
    logger.info("Generating user prompt for brochure generation...")
    user_prompt = (
        f"You are looking at a company called: {company_name}\n"
        "Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n\n"
        f"{website.get_contents()}"
    )
    return user_prompt[:7000]  # Truncate to prevent overly long prompts
