"""Build the CV.

Reads cv/cv.html (the single source of truth) and produces:
  cv/Erick_Casanova_CV.pdf   the printable two-page PDF
  site/                      the web version published to GitHub Pages

Run locally:
  pip install -r scripts/requirements.txt && python -m playwright install chromium
  python scripts/build_cv.py
"""

from pathlib import Path
import shutil
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
CV_DIR = ROOT / "cv"
SOURCE = CV_DIR / "cv.html"
PDF = CV_DIR / "Erick_Casanova_CV.pdf"
SITE = ROOT / "site"
MAX_PAGES = 2


def render_pdf() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(SOURCE.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(path=str(PDF), format="Letter", prefer_css_page_size=True, print_background=True)
        browser.close()
    return len(PdfReader(str(PDF)).pages)


def build_site() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    shutil.copy(SOURCE, SITE / "index.html")
    shutil.copy(CV_DIR / "headshot.jpg", SITE / "headshot.jpg")
    shutil.copy(PDF, SITE / PDF.name)


def main() -> None:
    pages = render_pdf()
    print(f"PDF written: {PDF.relative_to(ROOT)} ({pages} pages)")
    if pages > MAX_PAGES:
        sys.exit(f"CV is {pages} pages; keep it to {MAX_PAGES}. Trim content in cv/cv.html.")
    build_site()
    print(f"Site written: {SITE.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
