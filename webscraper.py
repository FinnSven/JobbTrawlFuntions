import requests
from bs4 import BeautifulSoup

def search_website(url, search_term):
    """
    Search for a term in the content of a website.

    :param url: URL of the website to scrape
    :param search_term: Term to search for in the website content
    :return: List of occurrences of the search term in the website content
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the website: {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    occurrences = []
    for line in text.split('\n'):
        if search_term.lower() in line.lower():
            occurrences.append(line.strip())

    return occurrences
import requests
from bs4 import BeautifulSoup

def search_website(url, search_term):
    """
    Search for a term in the content of a website.

    :param url: URL of the website to scraped
    :param search_term: Term to search for in the website content
    :return: List of occurrences of the search term in the website content
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the website: {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    occurrences = []
    for line in text.split('\n'):
        if search_term.lower() in line.lower():
            occurrences.append(line.strip())

    return occurrences
