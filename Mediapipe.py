def dibujar_piano(frame, teclas_activas):
    alto, ancho, _ = frame.shape
    num_teclas = 10
    tecla_ancho = ancho // num_teclas
    tecla_alto = 100  # Altura del piano en píxeles

    notas = ["Fa", "La", "Re", "Do", "Sol", "Si", "Do", "Mi", "Fa", "Sol"]
    for i in range(num_teclas):
        x1 = i * tecla_ancho
        x2 = x1 + tecla_ancho
        y1 = alto - tecla_alto
        y2 = alto

        color = (255, 255, 255)  # Blanco
        if teclas_activas[i]:
            color = (0, 255, 0)  # Verde si está activa

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)  # Borde negro
        cv2.putText(frame, notas[i], (x1 + 10, y2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
import cv2
import mediapipe as mp
import pygame

mp_manos = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

pygame.mixer.init()

sonidos = [
    pygame.mixer.Sound("sonidos/fa.wav"),   # Pulgar izquierdo 0
    pygame.mixer.Sound("sonidos/la.wav"),    # Índice izquierdo 1
    pygame.mixer.Sound("sonidos/re.wav"),    # Medio izquierdo 2
    pygame.mixer.Sound("sonidos/do.wav"),   # Anular izquierdo 3
    pygame.mixer.Sound("sonidos/sol.wav"),  # Meñique izquierdo 4
    pygame.mixer.Sound("sonidos/si.wav"),    # Pulgar derecho 5
    pygame.mixer.Sound("sonidos/do.wav"),    # Índice derecho 6
    pygame.mixer.Sound("sonidos/mi.wav"),    # Medio derecho 7
    pygame.mixer.Sound("sonidos/fa.wav"),    # Anular derecho 8
    pygame.mixer.Sound("sonidos/sol.wav"),   # Meñique derecho 9
]

def is_finger_down(ladmarks, finger_tip,finger_mcp):
    return ladmarks[finger_tip].y > ladmarks[finger_mcp].y

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

with mp_manos.Hands( min_detection_confidence = 0.5, min_tracking_confidence = 0.5,
                    max_num_hands = 2) as hands:
    finger_states = [False]*10 #Estado de los dedos (5 por mano)

    while cap.isOpened():# Bucle de Captura de video
        ret, frame = cap.read()
        if not ret:
            print("No se puede recibir frame (stream end?). Saliendo ...")
            break
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        teclas_activas = [False]*10
        if results.multi_hand_landmarks:
            for mano, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_manos.HAND_CONNECTIONS)

                finger_tips = [4, 8, 12, 16, 20]
                finger_mcps = [3, 7, 11, 15, 19]

                for i in range(5):
                    finger_index = i + mano * 5
                    if finger_index < len(finger_states) and finger_index < len(teclas_activas):
                        if is_finger_down(hand_landmarks.landmark, finger_tips[i], finger_mcps[i]):
                            if not finger_states[finger_index]:
                                sonidos[finger_index].play()
                                finger_states[finger_index] = True
                            teclas_activas[finger_index] = True
                        else:
                            finger_states[finger_index] = False

        dibujar_piano(frame, teclas_activas)
        cv2.imshow('Manos detectadas ', frame)
        if cv2.waitKey(1) & 0xFF ==  27:
            break

cap.release()
cv2.destroyAllWindows()