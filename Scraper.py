from bs4 import BeautifulSoup
import requests

_base_link = "https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_detail_sched?term_in=202408&crn_in="

def check_available(crn):

    full_link = _base_link + crn  #add course number to url

    #get html content for url
    try:
        response = requests.get(full_link)
        html = BeautifulSoup(response.text, 'html.parser')
        soup = html.find('table',class_="datadisplaytable")

        seat_areas = soup.find('table',class_="datadisplaytable")

        #find all rows within seating area
        rows = seat_areas.find_all('tr')

        #find all td elements 
        td_elements = (rows[0].find_all('td',class_='dddefault'))

        if len(td_elements) >=3:
                remaining_seats = int(td_elements[2].get_text(strip=True))
        
        return remaining_seats > 0
    
    except Exception as e:
            print(f"Error: {e}")
            return False
