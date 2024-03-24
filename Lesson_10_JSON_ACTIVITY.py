import json
import urllib.request

def get_articles(month, year):
    """Fetches and displays the top 1000 most visited articles for a given month and year."""
    base_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/"
    endpoint = f"en.wikipedia.org/all-access/{year}/{month}/all-days"
    url = base_url + endpoint

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            articles = data["items"][0]["articles"]
            print(f"Top 1000 articles for {month}/{year}:")
            for i, article in enumerate(articles[:1000], 1):
                print(f"{i}. {article['article']} ({article['views']} views)")
            print("\n")
    except urllib.error.URLError as e:
        print(f"Error fetching data: {e}")

def main():
    
    for month in range(1, 13):
        articles = get_articles(month, 2023)
        if articles:
            print(f"Top 1000 articles for {month}/2023:")
            for i, article in enumerate(articles[:1000], 1):
                print(f"{i}. {article['article']} ({article['views']} views)")
            print("\n")
        else:
            print(f"No data available for {month}/2023\n")

main()
