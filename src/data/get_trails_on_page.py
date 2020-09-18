from soup_kitchen import make_soup
from get_region_urls import build_urls, BASE_URL

from bs4 import BeautifulSoup


def extract_url(td):
    return td.find('a',href=True)['href']


def extract_text(td):
    return td.find('a',href=True).text


def extract_id(url):
    trail_id = url.replace('https://www.trailforks.com/trails/','').replace('/','')
    return trail_id


def process_table(soup: BeautifulSoup):
    trail_name_soup = soup.tbody.find_all('td',class_='highlight')
    region_name_soup = soup.tbody.find_all('td',class_='nowrap')
    for trail, region in zip(trail_name_soup, region_name_soup):
        trail_url = extract_url(trail)
        trail_id = extract_id(trail_url)
        trail_name = extract_text(trail)
        region_url = extract_url(region)
        region_name = extract_text(region)
        yield trail_id, trail_name, trail_url, region_name, region_url


if __name__ == '__main__':
    import pandas as pd
    import pickle

    urls = build_urls(BASE_URL)
    df = pd.DataFrame(columns=['trail_id', 'trail_name', 'trail_url', 'region_name', 'region_url'])
    for url in urls:
        page_soup = make_soup(url)
        table = page_soup.find_all('table')[0]
        trail_gen = process_table(table)
        for i, tup in enumerate(trail_gen):
            df = df.append({
                'trail_id':tup[0], 
                'trail_name':tup[1],
                'trail_url':tup[2],
                'region_name':tup[3],
                'region_url':tup[4]
            }, ignore_index=True)
    with open('data/raw/trails_with_regions.pkl', 'wb') as f:
        pickle.dump(df, f)
        
    df.to_csv('data/raw/trails_with_regions.csv', index=False)
    
    



