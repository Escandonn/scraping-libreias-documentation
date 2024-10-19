### Ejemplos y casos de uso

#### Ejemplos oficiales
El repositorio de Puppeteer incluye una pequeña cantidad de ejemplos mantenidos por el equipo de Puppeteer. Sigue las instrucciones en el archivo README para ejecutar los ejemplos, que cubren casos de uso como la creación de archivos PDF a partir de sitios web, la captura de capturas de pantalla o la intercepción de solicitudes.

#### Conjunto de ejemplos
Encuentra una colección de ejemplos no estructurados en el repositorio dedicado a ejemplos de Puppeteer. Este conjunto ha ido creciendo con el tiempo y cubre varios casos de uso, como el reenvío de eventos desde el proceso de Puppeteer al navegador, la interacción con elementos y la ejecución de comandos CDP.

#### Otros proyectos, artículos y demostraciones
A continuación se muestra una lista de casos de uso y ejemplos en categorías como Renderizado, Raspado web y Pruebas.

### Renderizado y raspado web
- **Puppetron**: Sitio de demostración que muestra cómo usar Puppeteer y Chrome sin cabeza para renderizar páginas. Inspirado en GoogleChrome/rendertron.
- **Thal**: Comienza con Puppeteer y Chrome sin cabeza para raspado web.
- **pupperender**: Middleware de Express que verifica el encabezado User-Agent de las solicitudes entrantes y, si coincide con uno de un conjunto configurable de bots, renderiza la página usando Puppeteer. Útil para el renderizado de aplicaciones web progresivas (PWA).
- **headless-chrome-crawler**: Rastreador que proporciona APIs para manipular Chrome sin cabeza y permite rastrear sitios web dinámicos.
- **Ejemplos de Puppeteer de Checkly**: Ejemplos de Puppeteer para casos de uso reales, como obtener información útil de páginas web o escenarios comunes de inicio de sesión.
- **browserless**: Chrome sin cabeza como un servicio que te permite ejecutar scripts de Puppeteer de forma remota.
- **Puppeteer en AWS Lambda**: Ejecuta Puppeteer en AWS Lambda con el framework Serverless.
- **Apify SDK**: Biblioteca escalable de rastreo y raspado web para JavaScript. Gestiona automáticamente un conjunto de navegadores Puppeteer y proporciona manejo de errores, gestión de tareas, rotación de proxies, y más.

### Pruebas
- **angular-puppeteer-demo**: Repositorio de demostración que explica cómo usar Puppeteer en Karma.
- **mocha-headless-chrome**: Herramienta que ejecuta pruebas de Mocha del lado del cliente en la línea de comandos a través de Chrome sin cabeza.
- **puppeteer-to-istanbul-example**: Repositorio de demostración que muestra cómo generar la cobertura de Puppeteer en formato Istanbul.
- **jest-puppeteer**: Herramienta con (casi) cero configuración para configurar y ejecutar Jest y Puppeteer. También incluye una biblioteca de aserciones para Puppeteer.
- **puppeteer-har**: Genera archivos HAR con Puppeteer.
- **puppetry**: Aplicación de escritorio para construir pruebas impulsadas por Puppeteer y Jest sin necesidad de codificación.
- **puppeteer-loadtest**: Interfaz de línea de comandos para realizar pruebas de carga en scripts de Puppeteer.
- **cucumber-puppeteer-example**: Repositorio de ejemplo que demuestra cómo usar Puppeteer y Cucumber para pruebas de integración.

Estos proyectos muestran cómo Puppeteer puede facilitar el trabajo con renderizado de páginas, raspado de datos, pruebas automatizadas y otras tareas relacionadas con la automatización de navegadores.