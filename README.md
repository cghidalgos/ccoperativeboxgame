# ccoperativeboxgame - Juego Cooperativo en Flask y Socket.IO

**ccoperativeboxgame** es un juego multijugador cooperativo en tiempo real, desarrollado con Flask y Socket.IO, donde los jugadores controlan un "punto negro" que deben mover hacia un "punto naranja". Para lograrlo, los jugadores deben trabajar juntos, moviendo sus propios puntos (representados por círculos de colores) en el tablero. El objetivo es llegar al punto naranja, y el juego verifica automáticamente cuando los jugadores logran alcanzarlo.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python y las siguientes dependencias:

- **Flask**: Framework web de Python.
- **Flask-SocketIO**: Para manejar la comunicación en tiempo real entre el servidor y los clientes.
- **random**: Para generar posiciones aleatorias.
- **math**: Para calcular distancias entre puntos.

### Instalación de dependencias

1. Clona este repositorio:
    ```bash
    git clone https://github.com/cghidalgos/ccoperativeboxgame.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd ccoperativeboxgame
    ```

3. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

4. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## Cómo Jugar

1. **Página de inicio**: Los jugadores ingresan su nombre en la página principal (`index.html`).
2. **Unirse al juego**: Después de ingresar el nombre, los jugadores serán redirigidos al tablero de juego.
3. **Movimientos**: Los jugadores pueden mover su "punto" (círculo de color) usando los botones de dirección (arriba, abajo, izquierda, derecha).
4. **Objetivo**: El objetivo del juego es mover el "punto negro" hacia el "punto naranja". Todos los jugadores deben trabajar juntos para lograrlo.
5. **Victoria**: Cuando el "punto negro" llega al "punto naranja", se muestra un mensaje de victoria para todos los jugadores.
6. **Reiniciar**: Los jugadores pueden reiniciar el juego usando el botón correspondiente.

## Cómo Ejecutar la Aplicación

1. Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:

    ```bash
    python app.py
    ```

2. La aplicación estará disponible en [http://localhost:5003](http://localhost:5003).

## Descripción del Código

### `app.py`

El archivo principal de la aplicación, en el que se define el servidor Flask y las rutas del juego. También maneja las interacciones en tiempo real entre los clientes usando **Socket.IO**:

- **Flask**: Proporciona las rutas para las páginas del juego y la página de inicio.
- **Socket.IO**: Gestiona la comunicación en tiempo real, incluyendo el movimiento de los jugadores, el desplazamiento del "punto negro" y la comprobación de si el juego ha terminado.

### `index.html`

La página principal donde los jugadores ingresan su nombre para unirse al juego.

### `game.html`

El tablero del juego donde los jugadores interactúan con el "punto negro" y el "punto naranja". Incluye botones de movimiento y muestra el estado del juego, incluyendo la victoria.

## Características

- **Juego multijugador en tiempo real**: Los jugadores pueden unirse a la partida con un nombre único y ver a los demás jugadores en el tablero.
- **Interacción en tiempo real**: Los movimientos de los jugadores y la posición del punto negro se actualizan instantáneamente para todos los jugadores.
- **Cooperación entre jugadores**: Los jugadores deben colaborar para mover el punto negro hacia el punto naranja.
- **Victoria**: El juego se completa cuando el punto negro alcanza el punto naranja.
- **Reinicio**: Los jugadores pueden reiniciar el juego en cualquier momento.

## Funcionalidades Adicionales (Posibles Mejoras)

Este proyecto tiene espacio para mejorar y agregar nuevas funcionalidades como:

- **Chat en tiempo real**: Los jugadores pueden comunicarse entre sí durante el juego.
- **Contador de progreso**: Mostrar una barra de progreso o contador para indicar el avance hacia la victoria.
- **Efectos de animación**: Agregar animaciones de movimientos y transiciones en el juego para mejorar la experiencia visual.
- **Temporizador o límite de tiempo**: Añadir un temporizador para que los jugadores deban completar la tarea en un tiempo determinado.
- **Ajustes de dificultad**: Permitir que los jugadores ajusten la dificultad del juego (por ejemplo, cambiar el tamaño del objetivo o la velocidad de movimiento del "punto negro").
- **Número de usuarios conectados**: Mostrar cuántos usuarios están actualmente conectados al juego.

## Contribuciones

Si deseas contribuir al proyecto, siéntete libre de hacer un fork y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

BY GHS, BETA ... 
