import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "brochure"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/scraping.py",
    f"{project_name}/prompts.py",
    f"{project_name}/llm.py",
    f"{project_name}/brochure_builder.py",
    f"{project_name}/display.py",
    "main.py",
    "requirements.txt",
    ".env",
    "README.md",
    "tests/__init__.py",
    "tests/test_scraping.py",
    "tests/test_prompts.py",
    "tests/test_llm.py",
    "tests/test_brochure_builder.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")

logging.info(f"All files created successfully")