# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:46:01 2022

@author: rahma
"""

import cv2

#Memilih camera
cap = cv2.VideoCapture(0)

#Menentukan Resolusi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

#Mengubah warna cam menjadi BGR2HSV
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
#Besar titik pixel (cx dan cy)
    cx = int(width / 2)
    cy = int(height / 2)
    
#Letak titik pixel
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

#Mendefinisikan Mata Uang Berdasarkan Kode Hue (warnanya)
    color = "Undefined"
    if hue_value < 0:
        color = "MATA UANG"
    elif hue_value < 10:
        color = "5000 -> $0.33"
    elif hue_value < 30:
        color = "1000 -> $0.067"
    elif hue_value < 75:
        color = "20.000 -> $1.33"
    elif hue_value < 102:
        color = "2000 -> $0.13"
    elif hue_value < 105:
        color = "50.000 -> $3.34"
    elif hue_value < 160:
        color = "10.000 -> $0.67"
    elif hue_value < 177:
        color = "100.000 -> $6.67"
    else:
        color = "MATA UANG"
        
#mencetak nomor warna dalam kode hue
    print(hue_value)

#bagian titik di dalam video (diubah warnanya warnanya)
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])  

#Latar, Bagian Text, Circle
    cv2.rectangle(frame, (cx - 420, 120), (cx + 450, 20), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 400, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

#Menampilkan video
    cv2.imshow("Frame", frame)
    
#tekan q untuk menghentikan video
    if cv2.waitKey (1) == ord('q'):
        break
            
cap.release()
cv2.waitKey(0);
cv2.destroyAllWindowos();
cv2.waitKey(1)
