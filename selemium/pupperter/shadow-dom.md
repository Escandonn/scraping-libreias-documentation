**Shadow DOM: Desde la Teoría hasta la Práctica**

### 1. ¿Qué es el DOM?
El Document Object Model (DOM) es la estructura en forma de árbol que un navegador genera al cargar una página web. Cada nodo de este árbol representa un elemento HTML de la página, lo que permite acceder y manipular dinámicamente sus contenidos mediante JavaScript. Cuando se realiza un cambio en un elemento, el navegador actualiza el DOM para reflejar la modificación.

### 2. ¿Qué es el Shadow DOM?
El concepto de **Shadow DOM** surge para resolver la necesidad de encapsular y aislar componentes dentro de una página web. A diferencia del DOM global, donde cualquier cambio en el árbol afecta a la página entera, el Shadow DOM permite crear un "DOM en la sombra", que no interactúa con el DOM principal. Este aislamiento ayuda a:
- Encapsular estilos CSS.
- Encapsular scripts de JavaScript.
- Mantener el comportamiento de los componentes independiente del resto de la página.

**Ejemplo de Analogía**: 
Imagina que el árbol DOM principal es un árbol grande en el bosque. El Shadow DOM sería como una sombra de una rama de ese árbol, donde solo sus elementos específicos residen, sin afectar al árbol general.

### 3. ¿Cómo Crear un Shadow DOM?
Por defecto, los elementos HTML no tienen un Shadow DOM asociado. Para crearlo, debes usar el método `.attachShadow()` en un elemento HTML compatible.

```javascript
// Creación de un elemento <div>
const div = document.createElement("div");

// Adjunta un Shadow DOM en modo abierto
const shadow = div.attachShadow({ mode: "open" });
```

El método `.attachShadow()` recibe un objeto de opciones que define cómo se comportará el Shadow DOM. Las dos propiedades principales son:

- **mode**: Define el modo de encapsulación, siendo "open" (abierto) o "closed" (cerrado). El modo abierto permite acceder al Shadow DOM mediante la propiedad `.shadowRoot`, mientras que el modo cerrado oculta la referencia.
  
- **delegatesFocus**: Define si el Shadow DOM puede obtener el foco de forma automática.

### 4. Encapsulación con Shadow DOM

#### 4.1. Encapsulación de CSS
El Shadow DOM proporciona la capacidad de encapsular estilos, lo que significa que los estilos definidos en el interior del Shadow DOM no afectarán a los elementos externos y viceversa.

```javascript
class AppElement extends HTMLElement {
  constructor() {
    super();
    // Crear el Shadow DOM en modo abierto
    this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    // Insertar contenido en el Shadow DOM
    this.shadowRoot.innerHTML = /* html */`
      <style>
        span {
          background: steelblue;
          padding: 5px;
          color: white;
        }
      </style>
      <div>
        <p>¡Vuelve a la sombra, <span>CSS</span>! ¡NO... PUEDES... PASAR!</p>
      </div>
    `;
  }
}

// Registrar el componente
customElements.define("app-element", AppElement);
```

Con este código, el estilo aplicado al `<span>` dentro del componente no afectará a otros elementos `<span>` en el DOM de la página.

#### 4.2. Encapsulación de JavaScript
El Shadow DOM también aísla el JavaScript. Los selectores de JavaScript que se ejecutan en el DOM global no pueden acceder a elementos dentro del Shadow DOM.

### 5. Práctica: Creando un Componente con Shadow DOM

#### Paso 1: Crear el Archivo HTML
Crea un archivo `index.html` y define un contenedor donde se insertará el componente.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shadow DOM Tutorial</title>
</head>
<body>
  <h1>Ejemplo de Shadow DOM</h1>
  <app-element></app-element>
  
  <script src="app-element.js"></script>
</body>
</html>
```

#### Paso 2: Crear el Archivo JavaScript
Crea un archivo llamado `app-element.js` para definir el componente.

```javascript
class AppElement extends HTMLElement {
  constructor() {
    super();
    // Crear Shadow DOM en modo abierto
    this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    // Añadir contenido y estilos locales al Shadow DOM
    this.shadowRoot.innerHTML = `
      <style>
        p {
          font-size: 18px;
          color: #333;
        }
        span {
          background-color: #4CAF50;
          color: white;
          padding: 4px;
          border-radius: 3px;
        }
      </style>
      <p>¡Hola desde el <span>Shadow DOM</span>!</p>
    `;
  }
}

// Definir el nuevo elemento personalizado
customElements.define("app-element", AppElement);
```

#### Paso 3: Prueba el Componente
Abre el archivo `index.html` en tu navegador. Deberías ver el mensaje "¡Hola desde el Shadow DOM!" estilizado solo en el componente.

### 6. Conclusión
El Shadow DOM es una poderosa herramienta para desarrollar aplicaciones web modernas, ofreciendo una forma sencilla de encapsular y aislar componentes. Al aprender a utilizarlo, puedes crear aplicaciones escalables y mantenibles, donde el código CSS y JavaScript esté claramente segmentado y no interfiera con otros elementos.

### 7. Ejercicios Adicionales
- Prueba a modificar el código para crear un Shadow DOM en modo cerrado.
- Añade un evento de clic al componente y observa cómo el encapsulamiento afecta a la propagación de eventos.
- Experimenta con la opción `delegatesFocus` y observa su comportamiento.

¡Con esta guía, tienes las herramientas para comenzar a trabajar con el Shadow DOM y llevar tus habilidades de desarrollo web al siguiente nivel!