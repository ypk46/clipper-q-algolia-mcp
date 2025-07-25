from datetime import datetime

import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP
from newspaper import Article

# Initialize FastMCP server
mcp = FastMCP("Clipper")


@mcp.tool()
def open_link(url: str):
    """
    Open a URL and return the content of the article page.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
    except Exception:
        text = None

    if not text:
        # Fallback to BeautifulSoup if newspaper fails
        try:
            response = requests.get(url, timeout=10)
            content_type = response.headers.get("Content-Type", "")
            # Skip downloads (e.g., application/pdf, octet-stream, etc.)
            if (
                "application/" in content_type
                or "octet-stream" in content_type
                or "download" in url
            ):
                return ""

            # Try to extract main content
            # Prefer <article> tag, else fallback to body text
            soup = BeautifulSoup(response.text, "html.parser")
            main = soup.find("article")
            if main:
                text = main.get_text(separator=" ", strip=True)
            else:
                text = (
                    soup.body.get_text(separator=" ", strip=True) if soup.body else ""
                )
        except Exception:
            text = ""

    return text or ""


@mcp.tool()
def get_current_date():
    """
    Get the current date in a human-readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    mcp.run(transport="stdio")
