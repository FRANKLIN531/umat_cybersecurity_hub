import feedparser

# CVE RSS feed
rss_url = "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss-analyzed.xml"
feed = feedparser.parse(rss_url)

# Your actual page with HTML & Bootstrap layout
output_file = "cves.html"

# Load existing content (so we don’t overwrite everything)
with open(output_file, "r", encoding="utf-8") as f:
    original_html = f.read()

# Inject cards at a placeholder <!-- CVE_FEED_HERE -->
cards_html = ""
for entry in feed.entries[:5]:
    title = entry.title
    link = entry.link
    summary = entry.summary

    card = f"""
    <div class="card mb-3 border-0 shadow-sm">
        <div class="card-body">
            <h5 class="card-title">{title}</h5>
            <p class="card-text">{summary}</p>
            <a href="{link}" target="_blank" class="btn btn-danger">Read More</a>
        </div>
    </div>
    """
    cards_html += card + "\n"

# Replace the placeholder with actual cards
updated_html = original_html.replace("<!-- CVE_FEED_HERE -->", cards_html)

# Save back into the same cves.html
with open(output_file, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("✅ CVEs successfully added to cves.html")
