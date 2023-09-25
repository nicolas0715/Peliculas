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

peliculas = soup.find_all('div', {'class': 'js-tile-link'})
print(peliculas)

datos_peliculas = []
for pelicula in peliculas:
    nombre_pelicula = pelicula.find('span', {'data-qa': 'discovery-media-list-item-title'}).text.strip()
    fecha_streaming = pelicula.find('span', {'data-qa': 'discovery-media-list-item-start-date'}).text.strip()
    imagen = pelicula.find('img', {'class': 'posterImage'})['src']
    criticsscore = pelicula.find('score-pairs')['criticsscore']
    audiencescore = pelicula.find('score-pairs')['audiencescore']
    
    datos_pelicula = {
        'Nombre de la película': nombre_pelicula,
        'Fecha de streaming': fecha_streaming,
        'Imagen': imagen,
        'Puntuación de críticos': criticsscore,
        'Puntuación de la audiencia': audiencescore
    }
    
    datos_peliculas.append(datos_pelicula)



for idx, pelicula in enumerate(datos_peliculas, start=1):
    print(f"Película {idx}:")
    print(f"Nombre: {pelicula['Nombre de la película']}")
    print(f"Fecha de streaming: {pelicula['Fecha de streaming']}")
    print(f"Imagen: {pelicula['Imagen']}")
    print(f"Puntuación de críticos: {pelicula['Puntuación de críticos']}")
    print(f"Puntuación de la audiencia: {pelicula['Puntuación de la audiencia']}")
    print("\n")

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
    for p in datos_peliculas:
        file.write('<div class="pelicula">\n')
        file.write('<img alt="' + pelicula['Nombre de la película'] + '" height="90" src="' + pelicula['Imagen'] + '" width="68"/>\n')
        file.write(f'<p class="nombre">' + pelicula['Nombre de la película'] + '</p>\n')
        file.write(f"<p>Fecha de streaming: " + pelicula['Fecha de streaming'] + '</p>\n')
        file.write(f"<p>Puntuación de críticos: " + pelicula['Puntuación de críticos'] + '%</p>\n')
        file.write(f"<p>Puntuación de la audiencia: " + pelicula['Puntuación de la audiencia'] + '%</p>\n')
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
