from bs4 import BeautifulSoup
import requests
import random
from datetime import datetime
import os

from pushear import pushear_html
'''
directory = (os.environ['GITHUB_WORKSPACE'])
print('La ruta Raiz: ', directory)
file_path = os.path.join(directory[:-14], 'index.html') # Se le resto '/WebScrapping2' del final de la cadena
'''
file_path = 'index.html'

url = "https://www.rottentomatoes.com/browse/movies_at_home/affiliates:netflix~sort:audience_highest"  
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
#print(soup)

divs = soup.find_all('div', class_='js-tile-link')
links = soup.find_all('a', class_='js-tile-link')

datos_peliculas = []
for div, link in zip(divs, links):
    # Extrae los datos que necesitas de cada etiqueta
    nombre_pelicula = div.find('span', class_='p--small').get_text(strip=True)
    fecha_streaming = div.find('span', class_='smaller').get_text(strip=True)
    imagen = div.find('img')['src']
    criticsscore = link.find('score-pairs')['criticsscore']
    audiencescore = link.find('score-pairs')['audiencescore']

    pelicula = {
        'Nombre_película': nombre_pelicula,
        'Fecha_streaming': fecha_streaming,
        'Imagen': imagen,
        'Criticsscore': criticsscore,
        'Audiencescore': audiencescore
    }
    
    # Agrega el diccionario a la lista de datos de películas
    datos_peliculas.append(pelicula)

print(datos_peliculas)

with open(file_path, 'w') as file:
    print('Inicia a crear el HTML')
    file.write('<!DOCTYPE html>\n')
    file.write('<html lang="es">\n')
    file.write('<head>\n')
    file.write('<meta charset="UTF-8">\n')
    file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    file.write('<title>Pelis</title>\n')
    file.write('<link rel="stylesheet" href="./index.css">\n')
    file.write('</head>\n')
    file.write('<body>\n')
    
    file.write(f'<p class="fecha">Ultima Actualizacion: {(datetime.now()).strftime("%d/%m/%y, %H:%M:%S")}</p>\n')
    
    file.write('<h2>Peliculas</h2>\n')
    file.write('<div class="peliculas">\n')
    for pelicula in datos_peliculas:
        file.write('<div class="pelicula">\n')
        file.write('<img alt="' + pelicula['Nombre_película'] + '" height="90" src="' + pelicula['Imagen'] + '" width="68"/>\n')
        file.write(f'<p class="nombre">' + pelicula['Nombre_película'] + '</p>\n')
        file.write(f"<p>Fecha de streaming: " + pelicula['Fecha_streaming'] + '</p>\n')
        file.write(f"<p>Puntuación de críticos: " + pelicula['Criticsscore'] + '%</p>\n')
        file.write(f"<p>Puntuación de la audiencia: " + pelicula['Audiencescore'] + '%</p>\n')
        file.write('</div>\n')
    file.write('</div>\n')
    file.write('</body>\n')
    file.write('</html>\n')
    print('Termina de crear el HTML')

print("Ruta del archivo HTML:", file_path) 

#Ruta raiz
ruta_raiz = os.getcwd()

carpeta_id = '1ckVvGyKhzw9fA9Sen-dsUY2Kh60jUGO9'

pushear_html()
