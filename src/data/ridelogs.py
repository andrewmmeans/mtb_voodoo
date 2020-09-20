from .soup_kitchen import make_soup
from bs4.element import Tag


def extract_trail_ids_from_tag(tag):
    """Extract trail_id from tag
    Args:
        tag: Tag
    Returns:
        url: str
    """
    url = tag.attrs.get('href')
    return url


def extract_rides_past_week(soup):
    """Extract number of rides in past week from page
    
    Args:
        soup: BeautifulSoup
    
    Returns:
        rides: int
    """
    rides = 0
    try:
        rides = int(soup.select('.block > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > b:nth-child(1)')[0].text)
    except Exception as e:
        print(e)
    return rides


def extract_rides_six_months(soup):
    """Extract number of rides in past six months from page
    
    Args:
        soup: BeautifulSoup
    
    Returns:
        rides: int
    """    
    rides = 0
    try:
        rides = int(soup.select('.block > div:nth-child(2) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > b:nth-child(1)')[0].text)
    except Exception as e:
        print(e)
    return rides


def extract_rides_total(soup):
    """Extract number of rides total from page
    
    Args:
        soup: BeautifulSoup
    
    Returns:
        rides: int
    """    
    rides = 0
    try:
        rides = int(soup.select('.block > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > b:nth-child(1)')[0].text)
    except Exception as e:
        print(e)
    return rides


def ride_log_summary(soup):
    """Creates trail ride log summary from page
    
    Args:
        soup: BeautifulSoup
    Returns:
        ride_log_sum_dict: Dict
    """
    ride_log_sum_dict = {
        'rides_past_week': extract_rides_past_week(soup),
        'rides_six_months': extract_rides_six_months(soup),
        'rides_total': extract_rides_total(soup)
    }
    return ride_log_sum_dict


def process_single_ridelog(soup):
    split_trail_rides = []
    
    table = soup.find('section').find('table',id='').find('tbody').find_all('tr')

    # store all riding attributes
    ride_date = []
    rider_url = []
    rider_name = []
    trails_ridden = []
    ride_difficulty_string = []


    for row in table:
        row_struct = row.find_all('td')
        ride_date.append(row_struct[1].find('span').text)
        # this year's rides don't include the year, append it
        ride_date = [x + ', 2020' if ',' not in x else x for x in ride_date]
        rider_url.append(row_struct[2].find('a').attrs['href'])
        rider_name.append(row_struct[2].find('a').text)
        
        # there can be multiple trails listed in a ride log
        trail_urls = []
        for tag in row_struct[4]:
            if type(tag) is Tag:
                trail_id = extract_trail_ids_from_tag(tag).split('/')[-2]
                if trail_id != 'achievements':
                    trail_urls.append(trail_id)
        
        trails_ridden.append(trail_urls)
        try:
            ride_difficulty_string.append(row_struct[5].span.attrs['title'])
        except AttributeError:
            ride_difficulty_string.append('Unknown')

    # this expansion of rows may need to be reworked to avoid duplication
    for i, comb in enumerate(zip(ride_date, rider_url, rider_name, trails_ridden, ride_difficulty_string)):
        for trail in comb[3]:
            split_trail_rides.append([comb[0], comb[1], comb[2], trail, comb[4]]) 

    return split_trail_rides

def get_all_ridelogs(trail_url):

    soup = make_soup(trail_url + 'ridelogs/')
    # parse max page from pagination
    max_page = int(soup.select('.pageNumbers')[0].select('a')[-1].text)
    ride_logs = []
    ride_logs.append(process_single_ridelog(soup))
    if max_page > 1:
        for i in range(max_page):
            nth_page = i + 1
            built_url = f'{trail_url}ridelogs/?activitytype=1&page={nth_page}'
            soup = make_soup(built_url)
            ride_logs.append(process_single_ridelog(soup))
    return ride_logs