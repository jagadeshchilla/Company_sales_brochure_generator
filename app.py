# app.py

import os
from flask import Flask, render_template, request
from brochure.brochure_builder import stream_brochure
import markdown as md

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    brochure_html = None
    error = None

    if request.method == "POST":
        company_name = request.form.get("company_name")
        website_url = request.form.get("website_url")

        if not company_name or not website_url:
            error = "Please fill in all fields."
        else:
            try:
                markdown_text = stream_brochure(company_name, website_url, stream=False)
                brochure_html = md.markdown(markdown_text, extensions=["extra", "smarty"])
            except Exception as e:
                error = f"Error generating brochure: {str(e)}"

    return render_template("index.html", brochure=brochure_html, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

