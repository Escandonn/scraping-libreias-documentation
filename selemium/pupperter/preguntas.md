### Preguntas frecuentes

#### P: ¿Quién mantiene Puppeteer?
R: El equipo de Automatización del Navegador Chrome mantiene la biblioteca, ¡pero nos encantaría recibir tu ayuda y experiencia en el proyecto! Consulta nuestra guía de contribución.

#### P: ¿Cuál es el estado del soporte para navegadores cruzados?
R: A partir de Puppeteer v23.0.0, Puppeteer ofrece soporte tanto para Chrome como para Firefox.

Para automatizar Chrome, Puppeteer utiliza el Protocolo de DevTools de Chrome (CDP) por defecto, pero también se puede automatizar utilizando WebDriver BiDi, que es el predeterminado para la automatización de Firefox.

Para comprender las sutiles diferencias en el soporte de API, consulta nuestra guía de WebDriver BiDi.

#### P: ¿Puppeteer soporta WebDriver BiDi?
R: Desde la versión v23.0.0 en adelante, Puppeteer tiene soporte en producción para WebDriver BiDi, lo que permite automatizar tanto Chrome como Firefox.

#### P: ¿Puppeteer seguirá soportando CDP?
R: No dejaremos de soportar la automatización de Chrome con CDP, a pesar del soporte de Puppeteer para WebDriver BiDi. Queremos evitar romper las automatizaciones existentes que dependen de CDP y continuar permitiendo casos de uso de automatización únicos para Chrome que no están estandarizados con WebDriver BiDi.

#### P: ¿Cuáles son los objetivos y principios de Puppeteer?
R: Los objetivos del proyecto son:

- Proporcionar una implementación de referencia que destaque las capacidades de los protocolos de DevTools de Chrome y WebDriver BiDi.
- Incrementar la adopción de pruebas automatizadas en navegadores cruzados.
- Ayudar a probar nuevas características del Protocolo de DevTools y WebDriver BiDi, ¡y encontrar errores!
- Aprender sobre los puntos problemáticos de las pruebas automatizadas en navegadores y ayudar a cubrir esas brechas.

Adaptamos los principios de Chromium para guiar nuestras decisiones de producto:

- **Velocidad**: Puppeteer tiene casi cero sobrecarga de rendimiento en una página automatizada.
- **Seguridad**: Puppeteer opera fuera del proceso del navegador, lo que lo hace seguro para automatizar páginas potencialmente maliciosas.
- **Estabilidad**: Puppeteer no debería ser inestable ni generar fugas de memoria.
- **Simplicidad**: Puppeteer proporciona una API de alto nivel que es fácil de usar, entender y depurar.

#### P: ¿Es Puppeteer un reemplazo para Selenium?
R: Puppeteer es una implementación de referencia basada en Node.js para automatizar navegadores con CDP y WebDriver BiDi, los mismos estándares web a los que el proyecto Selenium también contribuye.

El proyecto Selenium va más allá de lo que Puppeteer ofrece en múltiples aspectos: proporciona enlaces para más lenguajes que solo JavaScript y, por ejemplo, también ofrece herramientas para orquestar la automatización a gran escala, como Selenium Grid. Ambas cosas están fuera del alcance de Puppeteer.

Hay proyectos comunitarios que añaden capacidades a Puppeteer más allá de su núcleo, facilitando tareas como las pruebas. Por ejemplo, consulta:

- **jest-puppeteer** o
- **La integración de Puppeteer con Angular**

#### P: ¿Por qué Puppeteer v.XXX no funciona con una versión específica de Chrome o Firefox?
R: Cada versión de Puppeteer está estrechamente vinculada con una versión específica del navegador para garantizar la compatibilidad con la implementación de los protocolos subyacentes, el Protocolo de DevTools de Chrome y WebDriver BiDi. Esto es para evitar que cambios en Chrome o Firefox rompan inesperadamente Puppeteer.

#### P: ¿Qué versiones de Chrome y Firefox usa Puppeteer?
R: Busca las entradas de Chrome y Firefox en el archivo `revisions.ts`.

#### P: ¿Qué se considera una "navegación"?
R: Desde el punto de vista de Puppeteer, "navegación" es cualquier cosa que cambie la URL de una página. Además de la navegación regular en la que el navegador se conecta a la red para obtener un nuevo documento del servidor web, esto incluye las navegaciones con anclas y el uso de la API de historial.

Con esta definición de "navegación", Puppeteer funciona sin problemas con aplicaciones de una sola página (SPA).

#### P: ¿Cuál es la diferencia entre un evento de entrada "confiable" y "no confiable"?
R: En los navegadores, los eventos de entrada pueden dividirse en dos grandes grupos: confiables vs. no confiables.

- **Eventos confiables**: eventos generados por los usuarios interactuando con la página, por ejemplo, usando un ratón o teclado.
- **Eventos no confiables**: eventos generados por APIs web, como los métodos `document.createEvent` o `element.click()`.

Los sitios web pueden distinguir entre estos dos grupos:

- Usando el indicador de evento `Event.isTrusted`
- Detectando eventos acompañantes. Por ejemplo, cada evento de 'click' confiable es precedido por eventos 'mousedown' y 'mouseup'.

Para fines de automatización, es importante generar eventos confiables. Todos los eventos de entrada generados con Puppeteer son confiables y disparan los eventos acompañantes adecuados. Si, por alguna razón, se necesita un evento no confiable, siempre es posible usar `page.evaluate` para generar un evento falso:

```javascript
await page.evaluate(() => {
  document.querySelector('button[type=submit]').click();
});
```

#### P: ¿Puppeteer soporta la reproducción de medios y audio?
R: Puppeteer usa los binarios de Chrome para Testing por defecto, los cuales incluyen soporte para códecs propietarios a partir de la versión M120.

#### P: Tengo problemas para instalar/ejecutar Puppeteer en mi entorno de prueba. ¿Dónde puedo buscar ayuda?
R: Tenemos una guía de solución de problemas para varios sistemas operativos que enumera las dependencias necesarias.

#### P: ¡Tengo más preguntas! ¿Dónde puedo preguntar?
R: Hay muchas formas de obtener ayuda con Puppeteer:

- Para preguntas: [Stack Overflow](https://stackoverflow.com/)
- Para informes de errores: [GitHub Issues](https://github.com/)

Asegúrate de buscar en estos canales antes de publicar tu pregunta.