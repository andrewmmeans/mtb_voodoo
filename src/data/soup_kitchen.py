from bs4 import BeautifulSoup
from requests import get


def make_soup(url: str) -> BeautifulSoup:
    """
    Takes a provided url and returns a bs4.BeautifulSoup object
    Provides a header avoid status code 405 results

    Parameters
    ----------
    url: str
        A string URL

    Returns
    -------
    soup: BeautifulSoup
        A BeautifulSoup object
    """
    # Build a header dictionary
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

    # Get the response using the headers
    response = get(url,headers=headers)

    # Parse the content using HTML parsing
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup


