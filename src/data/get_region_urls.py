from soup_kitchen import make_soup
import numpy as np
import pandas as pd
import logging

BASE_URL = 'https://www.trailforks.com/region/washington/trails/'


def build_urls(base_url: str):
    """
    A url generator for a given region, as represented by the base_url
    Finds the maximum page count for a region and yields base_urls with page nums

    Args:
        base_url (str): A url for a region, i.e. Washington

    Yields:
        url (str): A url including page number
    """
    trail_soup = make_soup(base_url)
    pagination = trail_soup.find('ul', class_='paging-middle centertext').find_all('li')
    max_page = int(pagination[-1].text)
    for i in range(max_page):
        if i > 0:
            url = f'{base_url}?page={i+1}'
        else:
            url = base_url
        yield url




if __name__ == '__main__':
    urls = build_urls(BASE_URL)

