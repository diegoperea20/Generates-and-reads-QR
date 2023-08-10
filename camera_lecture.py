import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Inicializa la cámara
cap = cv2.VideoCapture(0)  # El valor 0 representa la cámara predeterminada

while True:
    # Captura un fotograma de la cámara
    ret, frame = cap.read()

    # Decodifica los códigos QR presentes en el fotograma
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        print("Contenido del código QR:", data)
        
        # Obtiene las coordenadas de los vértices del código QR
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            cv2.polylines(frame, [hull], True, (0, 255, 0), 3)
        else:
            cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 3)

    # Muestra el fotograma con los códigos QR detectados y el cuadrado verde
    cv2.imshow("Códigos QR en tiempo real", frame)

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
