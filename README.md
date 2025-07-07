# 🧠 AI-Powered Company Brochure Generator

### 🚀 Problem Statement

Create a product that builds a **brochure for a company** to be used for prospective **clients**, **investors**, and **potential recruits**.

We will be provided a **company name** and their **primary website**.

---

## 🧾 What is a Company Brochure?

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

## ✅ What Have We Built?

We’ve developed an end-to-end **AI-powered Flask web application** that:

- Accepts **company name** and **URL**
- Scrapes useful content (landing page, about, careers, etc.)
- Sends the content to **Gemini/Gemma 3 27B** for brochure generation
- Displays the brochure **live on the webpage**
- Supports **typing animation**, **loading spinners**, and **modern UI**
- Optionally saves the brochure as `README.md` for reuse

---

## 💻 Tech Stack Used

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

## 🛠️ Git Clone & Installation

```bash
git clone https://github.com/your-username/company-brochure-generator.git
cd company-brochure-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```
## 🔐 Add .env file:

```bash
GEMINI_API_KEY=your_gemini_or_gemma_api_key
```
## 🌐 Run the App
```bash
python app.py
```
Then open `http://localhost:5000` in your browser.

## Deployment
