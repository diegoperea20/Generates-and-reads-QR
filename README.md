# Generates and reads QR

<p align="justify">
Generates a QR code for a given URL using the qrcode library. It provides the ability to customize various aspects of the QR code, such as version, error correction level, size, and colors. The generated QR code is saved as an image file and capture real-time video from the default camera and decode QR codes present in the captured frames. Detected QR codes are highlighted with a green square, and their contents are printed in the console.
</p>

<p align="center">
  <img src="codigo_qr.png" alt="StepLast">
</p>

## Optional steps to implement

1. Use Dockerfile 
2. Use virtual enviroments and apply  requirements.txt 
```python
#virtual enviroment with conda 
conda create -n my_enviroment python=3.11.4

pip install -r requirements.txt
```