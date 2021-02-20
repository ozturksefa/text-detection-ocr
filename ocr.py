import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\sefaozturk\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.png') #resmi okuyoruz
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #resmi RGBye dönüştürüyoruz
#pytesseract

##### Karakterleri Yazdırma  ######
print(pytesseract.image_to_string(img)) # resimdeki tüm stringleri console da gösterir



### Karakter Tespiti  ######
yukseklik, genislik, _ = img.shape   
kutu = pytesseract.image_to_boxes(img)
for b in kutu.splitlines():
    print(b)
    b = b.split(' ') # listeye dönüştürdük 
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, yukseklik - y), (w, yukseklik - h), (50, 50, 255), 2)
    cv2.putText(img, b[0], (x, yukseklik - y+25),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)




# ##### Rakamları tespit etme ######
# yukseklik, genislik,_ = img.shape
# conf = r'--oem 3 --psm 6 outputbase digits' # oem .> motor modu default kullandık psm-> sayfa segmetnasyonu default 6 kullandık
# kutu = pytesseract.image_to_boxes(img,config=conf)
# for b in kutu.splitlines():
#     print(b)
#     b = b.split(' ')
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,yukseklik- y), (w,yukseklik- h), (50, 50, 255), 2)
#     cv2.putText(img,b[0],(x,yukseklik- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)




##### Kameradan tespit etme######
# alan = cv2.VideoCapture(0)
# alan.set(3,640)
# alan.set(4,480)
# def EkranAlanı(bbox=(300,300,1500,1000)):
#     ekran = np.array(ImageGrab.grab(bbox))
#     ekran = cv2.cvtColor(ekran, cv2.COLOR_RGB2BGR)
#     return ekran
# while True:
#     timer = cv2.getTickCount()
#     _,img = alan.read()

#     #karakter tespiti
#     yukseklik, genislik,_ = img.shape
#     kutu = pytesseract.image_to_boxes(img)
#     for b in kutu.splitlines():
#         #print(b)
#         b = b.split(' ')
#         print(b)
#         x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#         cv2.rectangle(img, (x,yukseklik- y), (w,yukseklik- h), (50, 50, 255), 2)
#         cv2.putText(img,b[0],(x,yukseklik- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
#     fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
#     cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
#     cv2.imshow("Result",img)
#     cv2.waitKey(0)



cv2.imshow('img', img)
cv2.waitKey(0)
