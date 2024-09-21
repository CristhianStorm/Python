from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# Configuración de las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Iniciar Chrome maximizado
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')  # Descomentar para modo sin interfaz gráfica

# Inicializa el servicio de ChromeDriver
service = Service(chromedriver_path)
chromedriver_path = r'C:\Users\Crisman\Documents\Python\Prueba\chromedriver.exe'
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre la URL de Jaguarete
driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')

try:
    # Espera a que los campos de código y contraseña estén presentes
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'codigo'))).send_keys("2022100592")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys("1245678")
    
    # Espera a que el botón de ingresar esté clickable y haz clic en él
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Ingresar"]'))).click()

    # Verifica si el inicio de sesión fue exitoso
    sleep(5)  # Opcional: esperar unos segundos para que la página cargue
    if "dashboard" in driver.current_url:  # Cambia "dashboard" según la URL esperada
        print("Inicio de sesión exitoso")
    else:
        print("Error en el inicio de sesión")

except NoSuchElementException as e:
    print(f"Error al encontrar un elemento: {e}")

finally:
    # Cierra el navegador
    driver.quit()
