# Automatización con Selenium: Crear un script que automatice tareas en un navegador web utilizando Selenium.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuramos el WebDriver con ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeELwUD-QjTbetNqssLAYXzlz3WD-8GpomHrRjBiUAgEu9v1w/viewform?usp=sf_link"
    driver.get(url)

    # Esperamos que el formulario se cargue correctamente

    time.sleep(1)

    # Llenamos los campos NOMBRE, EMAIL y MENSAJE

    campo_nombre = driver.find_element("xpath", '//input[@type="text" and @aria-labelledby="i1"]')
    campo_nombre.send_keys("Sebastián Huaypar")

    campo_email = driver.find_element("xpath", '//input[@type="text" and @aria-labelledby="i5"]')
    campo_email.send_keys("sebastianhuaypar93@gmail.com")

    campo_mensaje = driver.find_element("xpath", '//textarea[@aria-labelledby="i9"]')
    campo_mensaje.send_keys("Hola! Este es un mensaje de prueba")

    # Esperamos a que se complete correctamente

    time.sleep(1)

    # Indicamos que se de click al botón Enviar

    boton_enviar = driver.find_element("xpath", '//div[@role="button" and .//span[text()="Enviar"]]')
    boton_enviar.click()

    # Esperamos a que se envíe para comprobar que se haya ejecutado.

    time.sleep(2)

    confirmacion = driver.find_element("xpath", '//*[contains(text(), "El formulario se ha enviado correctamente")]')
    if confirmacion:
        print("Formulario enviado exitosamente.")
    else:
        print("No se pudo verificar el envío del formulario.")

except Exception as e:
    print(f"Error al llenar el formulario: {e}")

finally:
    driver.quit()