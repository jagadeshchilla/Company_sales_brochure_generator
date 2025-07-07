# AI-Powered Company Brochure Generator

### Problem Statement

Create a product that builds a **brochure for a company** to be used for prospective **clients**, **investors**, and **potential recruits**.

We will be provided a **company name** and their **primary website**.

---

## What is a Company Brochure?

A **company brochure** is a brief, informative document or webpage that outlines key aspects of an organization, such as:

- About Us / Mission
- Services / Products
- Clients / Partners
- Career Opportunities
- Company Culture
- Contact Information

It is typically shared with external audiences like:
- Customers
- Investors
- Job candidates

---

## What Have We Built?

We’ve developed an end-to-end **AI-powered Flask web application** that:

- Accepts **company name** and **URL**
- Scrapes useful content (landing page, about, careers, etc.)
- Sends the content to **Gemini/Gemma 3 27B** for brochure generation
- Displays the brochure **live on the webpage**
- Supports **typing animation**, **loading spinners**, and **modern UI**
- Optionally saves the brochure as `README.md` for reuse

---

## Tech Stack Used

| Category         | Tool / Library             |
|------------------|----------------------------|
| Language         | Python                     |
| Frontend         | HTML5, CSS3, Bootstrap 5   |
| Backend          | Flask                      |
| Web Scraping     | Requests, BeautifulSoup    |
| AI / LLM         | Google Generative AI (Gemini 1.5 / Gemma 3 27B) |
| Markdown Parsing | `markdown` (Python lib)    |
| Styling Fonts    | Google Fonts (Inter)       |
| Animations       | CSS Keyframes              |

---

## Git Clone & Installation

```bash
git clone https://github.com/your-username/company-brochure-generator.git
cd company-brochure-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```
## Add .env file:

```bash
GEMINI_API_KEY=your_gemini_or_gemma_api_key
```
## Run the App
```bash
python app.py
```
Then open `http://localhost:5000` in your browser.

## Deployment on Render

The project is live at:  
🔗 **[https://company-sales-brochure-generator.onrender.com](https://company-sales-brochure-generator.onrender.com)**

### 🔧 Manual Deployment Steps

> Render is a cloud platform that lets you deploy full-stack web apps with ease.

#### 1. Push your project to GitHub
Ensure your project includes:
- `app.py`
- `requirements.txt`
- `render.yaml` (explained below)
- All related source files (like `brochure/`, `templates/`, etc.)

#### 2. Create `render.yaml` in the root

```yaml
services:
  - type: web
    name: brochure-generator
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
    envVars:
      - key: GEMINI_API_KEY
        sync: false  # Set this manually in Render dashboard

```
>## Note on Model Usage

Due to **free trial limitations on Gemini API**, this project currently uses the **Gemma 3 27B IT** model for brochure generation.

While Gemma performs well for medium-length content, it has some constraints:

- Limited context window (can’t handle large sites well)
- Generates shorter brochures
- Slightly less fluent compared to Gemini Pro

### Want Better Results?

To generate **longer**, more detailed brochures with better understanding of full-page content:

**Upgrade to [Gemini Pro](https://ai.google.dev/gemini-api/docs/models/gemini) or Gemini 1.5 Flash**  
These models offer:

- Much **larger context windows** (up to 1M tokens)
- More **refined, structured responses**
- Faster streaming (especially Gemini 1.5 Flash)

### To Use Gemini Instead of Gemma:

1. Update your `.env`:

   ```env
   GEMINI_API_KEY=your_google_api_key
  ```

2. In llm.py, change:

```python

model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"

```
3. Restart the app or re-deploy

### Why Some Brochures Fail to Generate
Some websites (like claude.ai, openai.com, etc.) implement bot-blocking protections, which may cause the brochure generator to fail or return a 403 Forbidden error.

Common reasons:

- Cloudflare or CAPTCHA

- Blocked headers/user agents

- JavaScript-only rendering

- **What You Can Do:**
    - Try with more open/public sites (e.g., personal blogs, small startups)
    - Improve scraper with Playwright or Selenium (not included here)
    - Catch and handle blocked URLs with graceful error messages

