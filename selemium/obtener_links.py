from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Importa el servicio de Chrome

# Cambia esto por tu ruta de ChromeDriver
driver_path = "C:/Users/Laura/Documents/codigo/chromedriver_win32/chromedriver.exe"
url = 'https://nmap.org/book/toc.html'  # Cambia esto por la URL que deseas analizar

# Inicializa el servicio de Chrome
service = Service(driver_path)

# Inicializa el controlador
driver = webdriver.Chrome(service=service)

try:
    # Abre la página
    driver.get(url)

    # Encuentra todos los elementos de enlace
    links = driver.find_elements(By.TAG_NAME, 'a')

    # Extrae el texto y el href de cada enlace
    for link in links:
        text = link.text.strip()  # Texto del enlace
        href = link.get_attribute('href')  # URL del enlace
        if text:  # Asegúrate de que el texto no esté vacío
            print(f'Texto: "{text}" - URL: {href}')

finally:
    # Cierra el controlador
    driver.quit()
