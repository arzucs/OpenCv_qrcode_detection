import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret,img=cap.read()

    for barcode in decode(img):
        myData= barcode.data.decode('utf-8') #UTF-8 kodlama stilinde, farklı kod birimlerinden meydana gelecek biçimde iki tabanına dönüştürülür. 
        print(myData)
        
       #çokgen olmasının nedeni kamera olsa bile bir çokgen oluşturabilir.
        pts=np.array([barcode.polygon],np.int32) #
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (255,0,255), 3)
        pts2=barcode.rect #rectangle yazının bakodun köşesine yazılması için 
        cv2.putText(img, myData, (pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),1)
   
    cv2.imshow("qr",img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()