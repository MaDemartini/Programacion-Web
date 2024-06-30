# noticiero/cargar_noticias.py
from pathlib import Path
import os
from datetime import datetime
from bs4 import BeautifulSoup
from django.core.wsgi import get_wsgi_application
from django.core.files import File  # Para manejar archivos en Django

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caosNews.caosNews.settings')
application = get_wsgi_application()

# Importar modelos de Django
from noticiero.models import Noticia

# Función para cargar las noticias
def cargar_noticias():
    # Ruta donde se encuentran los archivos HTML de las noticias
    directorio_noticias = 'noticiero/templates/noticiero/noticias'

    # Iterar sobre los archivos en el directorio
    for filename in os.listdir(directorio_noticias):
        if filename.endswith('.html'):  # Asegurarse que son archivos HTML
            path = os.path.join(directorio_noticias, filename)
            with open(path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')

                # Extraer datos del HTML según la estructura
                titulo = soup.find('h2').text.strip()
                autor_fecha = soup.find('div', class_='info').text.strip()
                autor = autor_fecha.split('|')[0].strip().split(': ')[1]
                fecha_str = autor_fecha.split('|')[1].strip().split(': ')[1]
                fecha = datetime.strptime(fecha_str, '%d de %B, %Y').date()
                categoria = autor_fecha.split('|')[-1].strip().split(': ')[-1]
                contenido = '\n'.join([p.text.strip() for p in soup.find_all('p')])

                # Encontrar la imagen y obtener la ruta
                imagen_path = soup.find('img')['src']
                imagen_completa = os.path.join(directorio_noticias, imagen_path)

                # Verificar si la imagen existe localmente
                if Path(imagen_completa).is_file():
                    with open(imagen_completa, 'rb') as img_file:
                        imagen_django = File(img_file)

                        # Crear instancia de Noticia y guardar en la base de datos
                        noticia = Noticia(
                            titulo=titulo,
                            autor=autor,
                            fecha=fecha,
                            categoria=categoria,
                            contenido=contenido,
                            imagen=imagen_django
                        )
                        noticia.save()

if __name__ == '__main__':
    cargar_noticias()
