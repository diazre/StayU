#Se importan las librerias necesarias para realizar el scrapping
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#Se coloca el URL de búsqueda en Booking para Barcelona
url = 'https://www.booking.com/city/es/barcelona.es.html?aid=1610688;label=barcelona-bpyRqlXhE57qKfWJN8Jg7QS349939756727:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-123261865:lp9186193:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGZNq08ntPlxk;ws=&gclid=EAIaIQobChMIvbnoz-L8iAMV88vCBB0CdTLKEAAYASAAEgIeFvD_BwE'

#Se realiza la solicitud
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

#Se verifica si la solicitud fue exitosa
if response.status_code == 200:
	soup = BeautifulSoup(response.text, 'html.parser')

	#Buscando los datos que deseamos obtener
	properties = soup.find_all('div', class_='sr_property_block')

	data = []

	for prop in properties:
		#Extraemos el nombre de la propiedad
		name = prop.find('div', class_='f6431b446c a15b38c233').text.strip() if prop.find('div', class_='f6431b446c a15b38c233') else 'N/A'

		#Extraemos la direccion
		address = prop.find('a', class_='bui-link').text.strip() if prop.find('a', class_='bui-link') else 'N/A'

		#Extraemos el precio
		price = prop.find('span', class_='f6431b446c fbfd7c1165 e84eb96b1f').text.strip() if prop.find('span', class_='f6431b446c fbfd7c1165 e84eb96b1f') else 'N/A'

		#Extraemos la puntuación
		rating = prop.find('div', class_='bui-review-score__badge').text.strip() if prop.find('div', class_='bui-review-score__badge') else 'N/A'

		#Extaremos el número de habitaciones
		rooms = prop.find('div',class_='room-info').text.strip() if prop.find('div',class_='room-info') else 'N/A'

		data.append({
			'Nombre': name,
			'Dirección': address,
			'Precio': price,
			'Puntuación': rating,
			'Habitaciones': rooms
			})

		#Colocamos una pausa de 2 segundos entre cada solicitud
		time.sleep(2)

	#Creamos un dataframe de pandas
	df = pd.DataFrame(data)

	#Guardamos los datos en un archivo CSV
	df.to_csv('datos_booking_barcelona.csv', index=False)

	print("Datos Extraídos y guardados exitosamente!")

else:
	print("Error al realizar la solicitud:", response.status_code)