import os
from git import Repo


def pushear_html():
    # Ruta local al repositorio
    #repo_path = 'C:/Users/otero/Desktop/Pokio/Programacion/Proyectos/Proyectos_varios/Web_Scrapping4-'
    # Pero para ejecutarlo con Actions, necesito la ruta local
    ruta_raiz = os.getcwd()

    # Inicializar el repositorio
    repo = Repo(ruta_raiz)

    # Agregar los archivos al repositorio (opcional)
    repo.index.add('index.html')

    # Commit con un mensaje
    repo.index.commit('Commit desde script')
    
    token = os.getenv('NICO_TOKEN')

    # Realizar el push al repositorio remoto
    origin = repo.remote('origin')
    origin_url = origin.url.replace('https://', f'https://token:{token}@') 
    origin.set_url(origin_url)
    origin.push()