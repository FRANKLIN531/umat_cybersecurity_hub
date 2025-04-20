import feedparser

# List of RSS feeds
rss_feeds = {
    "SecurityWeek": "https://feeds.feedburner.com/Securityweek",
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/",
}

# Open the output file
with open("news_cards.html", "w", encoding="utf-8") as f:
    for source, url in rss_feeds.items():
        f.write(f'<h2 class="mt-4 mb-3">{source}</h2>\n<div class="row">\n')

        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # Top 3 articles per source
            title = entry.title
            link = entry.link
            summary = entry.summary if hasattr(entry, 'summary') else "No summary available."

            card_html = f"""
            <div class="col-md-4">
                <div class="card mb-4 shadow-sm border-0">
                    <div class="card-body">
                        <h5 class="card-title">{title}</h5>
                        <p class="card-text">{summary}</p>
                        <a href="{link}" target="_blank" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
            """
            f.write(card_html + "\n")
        
        f.write("</div>\n")  # Close the row

print("✅ News cards saved to news_cards.html")
