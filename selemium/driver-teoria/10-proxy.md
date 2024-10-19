Aquí tienes un tutorial completo sobre cómo utilizar la clase `Proxy` de Selenium para gestionar proxies en tus scripts de automatización. El tutorial cubre desde la teoría hasta la práctica, incluyendo ejemplos de código.

# Tutorial Completo sobre el Uso de Proxies en Selenium

## Introducción

En la automatización de navegadores web con Selenium, a menudo es necesario utilizar proxies para controlar la red de la aplicación o para acceder a contenido restringido geográficamente. Este tutorial explorará cómo implementar proxies en Selenium utilizando la clase `Proxy`.

## Requisitos Previos

Antes de comenzar, asegúrate de tener:

1. Python instalado en tu sistema.
2. Selenium instalado. Puedes instalarlo usando pip:

   ```bash
   pip install selenium
   ```

3. Un navegador web (por ejemplo, Chrome o Firefox) y su respectivo controlador (ChromeDriver o GeckoDriver) instalados.

## Conceptos Básicos

### ¿Qué es un Proxy?

Un proxy actúa como intermediario entre tu computadora y el servidor al que intentas acceder. Al usar un proxy, las solicitudes se envían al proxy primero, y este las reenvía al servidor de destino. Esto permite ocultar tu dirección IP real y acceder a contenido que puede estar bloqueado en tu ubicación.

### Tipos de Proxies

En Selenium, se pueden utilizar diferentes tipos de proxies que están definidos en la clase `ProxyType`. Algunos de los tipos de proxies disponibles son:

- **DIRECT**: Conexión directa sin proxy.
- **MANUAL**: Proxies configurados manualmente.
- **PAC**: Proxies configurados mediante un archivo de configuración automática.
- **AUTODETECT**: Detección automática de proxy.
- **SYSTEM**: Uso de la configuración del sistema.

## Implementación

### 1. Importar las Librerías Necesarias

Comienza importando las librerías necesarias:

```python
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
```

### 2. Configurar el Proxy

Puedes crear una instancia de la clase `Proxy` y configurar las propiedades necesarias, como el tipo de proxy y las direcciones de los proxies HTTP, SSL, FTP, etc.

```python
# Crear una instancia de Proxy
my_proxy = Proxy()
my_proxy.proxy_type = ProxyType.MANUAL
my_proxy.http_proxy = "http://mi_proxy_http:puerto"
my_proxy.ssl_proxy = "http://mi_proxy_ssl:puerto"
my_proxy.ftp_proxy = "http://mi_proxy_ftp:puerto"
my_proxy.no_proxy = "localhost,127.0.0.1"
```

### 3. Configurar el Navegador con el Proxy

Al crear el controlador del navegador (por ejemplo, Chrome), necesitas pasar la configuración del proxy a las capacidades del navegador.

#### Para Chrome:

```python
# Crear un objeto de opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={my_proxy.http_proxy}')

# Iniciar el navegador con el proxy configurado
driver = webdriver.Chrome(options=chrome_options)
```

#### Para Firefox:

```python
# Crear un objeto de perfil de Firefox
firefox_profile = webdriver.FirefoxProfile()

# Configurar el proxy
firefox_profile.set_preference("network.proxy.type", 1)  # Manual
firefox_profile.set_preference("network.proxy.http", "mi_proxy_http")
firefox_profile.set_preference("network.proxy.http_port", puerto)
firefox_profile.set_preference("network.proxy.ssl", "mi_proxy_ssl")
firefox_profile.set_preference("network.proxy.ssl_port", puerto)

# Iniciar el navegador con el perfil de proxy configurado
driver = webdriver.Firefox(firefox_profile=firefox_profile)
```

### 4. Navegar a una Página Web

Una vez que el navegador esté configurado con el proxy, puedes utilizar Selenium para navegar a una página web como de costumbre.

```python
# Navegar a una página web
driver.get("https://www.ejemplo.com")

# Esperar un momento para que se cargue la página
import time
time.sleep(5)  # Esperar 5 segundos

# Cerrar el navegador
driver.quit()
```

## Ejemplo Completo

Aquí hay un ejemplo completo de cómo usar un proxy con Selenium en Python.

```python
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Crear una instancia de Proxy
my_proxy = Proxy()
my_proxy.proxy_type = ProxyType.MANUAL
my_proxy.http_proxy = "http://mi_proxy_http:puerto"
my_proxy.ssl_proxy = "http://mi_proxy_ssl:puerto"
my_proxy.ftp_proxy = "http://mi_proxy_ftp:puerto"
my_proxy.no_proxy = "localhost,127.0.0.1"

# Configurar el navegador (Chrome en este caso)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={my_proxy.http_proxy}')

# Iniciar el navegador con el proxy configurado
driver = webdriver.Chrome(options=chrome_options)

# Navegar a una página web
driver.get("https://www.ejemplo.com")

# Esperar un momento para que se cargue la página
import time
time.sleep(5)  # Esperar 5 segundos

# Cerrar el navegador
driver.quit()
```

## Conclusión

Utilizar proxies en Selenium es una técnica valiosa para controlar el acceso a la red y ocultar la identidad. Con la clase `Proxy` y sus tipos, puedes configurar diferentes tipos de proxies fácilmente. Este tutorial cubre los aspectos básicos y proporciona un ejemplo práctico para ayudarte a comenzar. ¡Experimenta con diferentes configuraciones de proxy y adapta el código a tus necesidades!