import requests
from bs4 import BeautifulSoup

def search_websites(urls, search_term):
    """
    Search for a term in the content of multiple websites.

    :param urls: List of URLs of the websites to scrape
    :param search_term: Term to search for in the website content
    :return: Dictionary with URLs as keys and lists of occurrences of the search term as values
    """
    all_occurrences = {}

    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch the website: {url}")

        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        occurrences = []
        for line in text.split('\n'):
            if search_term.lower() in line.lower():
                occurrences.append(line.strip())

        all_occurrences[url] = occurrences

    return all_occurrences
