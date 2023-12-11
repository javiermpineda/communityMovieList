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

def find_facts(decription_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = decription_url
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find image elements in the parsed HTML
        facts_div = soup.find('div', class_='facts')

        if facts_div:
            # Extraer el texto dentro del elemento <span> y limpiar los espacios
            runtime_text = ' '.join(facts_div.stripped_strings)
            return runtime_text
        else:
            return "There is no description to show facts_div"
    else:
        return "There is no description to show conection 200"
        print(f"Error: Unable to retrieve search results. Status code: {response.status_code}")


def scrape_video_info(video_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Realiza la solicitud HTTP y obtén el contenido de la página
    response = requests.get(video_url, headers=headers)

    if response.status_code == 200:
        # Parsea el HTML con BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra la etiqueta que contiene la información del video
        video_link = soup.find('a', class_='play_trailer')

        # Extrae los atributos relevantes
        if video_link:
            video_id = video_link['data-id']
            video_title = video_link['data-title']
            video_site = video_link['data-site']
            video_url = f'https://www.{video_site}.com/watch?v={video_id}'

            # Retorna la información del video
            return {
                'title': video_title,
                'video_url': video_url,
            }
        else:
            return {'error': 'video link not found.'}
    else:
        return {'error': f'Error getting page. Status code: {response.status_code}'}

