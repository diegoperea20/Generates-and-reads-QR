import cv2
from pyzbar.pyzbar import decode

# Carga la imagen que contiene el código QR
image_path = "codigo_qr.png"
image = cv2.imread(image_path)
# Decodifica los códigos QR presentes en la imagen
decoded_objects = decode(image)

# Itera a través de los objetos decodificados y muestra los resultados
for obj in decoded_objects:
    data = obj.data.decode("utf-8")
    print("Contenido del código QR:", data)

# Muestra la imagen con los códigos QR detectados
cv2.imshow("Codigos QR Detectados", image)
cv2.waitKey(0)
cv2.destroyAllWindows()