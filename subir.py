
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

directorio = os.listdir()

carpeta_id = '1ckVvGyKhzw9fA9Sen-dsUY2Kh60jUGO9'

#Ruta raiz
ruta_raiz = os.getcwd() 
#repo_path = 'C:/Users/otero/Desktop/Pokio/Programacion/Proyectos/Proyectos_varios/Web_Scrapping4-'

def obtener_html(): #Obtener el archivo html
    archivo_html = [archivo for archivo in directorio if archivo.endswith('.html')]
    return archivo_html

def subir_html(carpeta_id, file_path):
    # Credenciales de Google Drive
    ruta_archivo_credenciales = os.path.join(ruta_raiz, 'driven-striker-386616-85af28be82bc.json') 
    credentials = service_account.Credentials.from_service_account_file(ruta_archivo_credenciales, scopes=['https://www.googleapis.com/auth/drive'])
    drive_service = build('drive', 'v3', credentials=credentials)

    # Eliminar cada archivo de la carpeta
    result = drive_service.files().list(q=f"'{carpeta_id}' in parents", fields="files(id)").execute()
    archivos = result.get('files', [])
    for archivo in archivos:
        drive_service.files().delete(fileId=archivo['id']).execute()
    
    media_body = MediaFileUpload(file_path, mimetype='text/plain', resumable=True)
    archivo_metadata = {'name': file_path, 'parents': [carpeta_id]}
    archivo = drive_service.files().create(body=archivo_metadata, media_body=media_body).execute()