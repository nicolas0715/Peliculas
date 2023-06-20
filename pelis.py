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

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"  
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

td_tags = soup.find_all("td", class_="titleColumn")

pelis = []
for td in td_tags:
    peli_d = {'numero': 0, 'nombre': '', 'ano': 0, 'imagen': 'url'}
    value = td.text.strip()            #Obtener el texto dentro de la etiqueta
    value_list = value.split('\n')     #Separarlos por el salto de linea.
    
    peli_d['numero'] = value_list[0][:-1]       #El primer valor es el numero. Y se le quita el punto del final
    peli_d['nombre'] = value_list[1].strip()    #El segundo valor es el nombre, que se le eliminan espacios antes y despues
    peli_d['ano'] = value_list[2].strip('()')   #El ultimo valor es el ano, que se le eliminan los parentesis que lo contienen.
    
    img_element = soup.find('img', alt= peli_d['nombre'])
    peli_d['imagen'] = img_element['src']
    
    pelis.append(peli_d)
print(pelis)

peli_random = random.choice(pelis)
with open(file_path, 'w') as file:
    print('Inicia a crear el HTML')
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('<meta charset="UTF-8">\n')
    file.write('<title>Pelis</title>\n')
    file.write('<link rel="stylesheet" href="./index.css">\n')
    file.write('</head>\n')
    file.write('<body>\n')
    
    file.write(f'<p class="fecha">Ultima Actualizacion: {(datetime.now()).strftime("%d/%m/%y, %H:%M:%S")}</p>\n')
    
    file.write('<h2>La Pelicula del Dia es:</h2>\n')
    file.write('<div class="pelicula">\n')
    file.write(f'<p>Nº ' + peli_random['numero'] + '</p>\n')
    file.write(f'<img alt="' + peli_random['nombre'] + '" height="67" src="' + peli_random['imagen'] + '" width="45"/>\n')
    file.write('<p class="nombre">' + peli_random['nombre'] + '</p>\n')
    file.write('<p>(' + peli_random['ano'] + ')</p>\n')
    file.write('</div>\n')
    
    file.write('<h2>Resto de las Peliculas</h2>\n')
    file.write('<div class="peliculas">\n')
    for p in pelis:
        file.write('<div class="pelicula">\n')
        file.write(f'<p>Nº ' + p['numero'] + '</p>\n')
        file.write(f'<img alt="' + p['nombre'] + '" height="67" src="' + p['imagen'] + '" width="45"/>\n')
        file.write('<p class="nombre">' + p['nombre'] + '</p>\n')
        file.write('<p>(' + p['ano'] + ')</p>\n')
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