import requests
from bs4 import BeautifulSoup

def find_description(decription_url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = decription_url
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find image elements in the parsed HTML
        overview_div = soup.find('div', class_='overview')

        # Verificar si se encontró el elemento antes de intentar extraer el texto
        if overview_div:
            # Encontrar el elemento <p> dentro del elemento <div>
            p_element = overview_div.find('p')

            if p_element:
                # Extraer el texto dentro del elemento <p>
                overview_text = p_element.get_text(strip=True)
                return overview_text

            else:
                return "There is no description to show"

        else:
            return "There is no description to show"
    else:
        return "There is no description to show"
        print(f"Error: Unable to retrieve search results. Status code: {response.status_code}")

