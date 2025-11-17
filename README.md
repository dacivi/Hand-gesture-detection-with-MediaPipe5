Actividad 5: Piano Virtual con Detección de Manos (MediaPipe)

Alumnos: 
AGUILAR GUSTAVO SALVADOR  
CARMONA CERNAS FLOR JAQUELINE 
CRUZ VILLANUEVA DANIEL 
HUITRON VARELA MIGUEL ANGEL 
GONZÁLES GONZÁLEZ ALAN EDUARDO 


Este proyecto es un piano virtual que se toca usando gestos de las manos, detectados en tiempo real a través de una cámara web.

Descripción

El programa utiliza la biblioteca OpenCV para capturar el video de la cámara web. La biblioteca MediaPipe (específicamente mp.solutions.hands) se usa para detectar los puntos de referencia (landmarks) de una o dos manos en el video.

Un piano simple se dibuja en la parte inferior de la pantalla usando funciones de cv2.

El programa detecta cuándo un dedo está "doblado" (comparando la coordenada Y de la punta del dedo con la de la articulación inferior) y activa la tecla correspondiente.

Los sonidos de las notas se manejan con Pygame Mixer, reproduciendo un archivo .wav diferente para cada dedo.

Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener Python 3 instalado, junto con las siguientes bibliotecas:

pip install opencv-python
pip install mediapipe
pip install pygame


Modo de Uso

Clona o descarga este repositorio.

Asegúrate de que la carpeta sonidos (con todos los archivos .wav) esté en el mismo directorio que el script de Python.

Ejecuta el script desde tu terminal:


Muestra tus manos a la cámara. Doblar un dedo hacia abajo simulará presionar una tecla y reproducirá una nota.

Presiona la tecla 'ESC' (Escape) para cerrar el programa.

Video de Demostración

https://youtu.be/-n_H-uL6lSM