import cv2
import numpy as np
from pyzbar.pyzbar import decode
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(0)


while True:
    ret,img=cap.read()

    cap.set(3,340)
    cap.set(4,480)
    
    griton=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian=cv2.Laplacian(img,cv2.CV_64F)
    sobel=cv2.Sobel(img,cv2.CV_64F, 0 ,1, ksize=5)
    sobely=cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize=5)
    gaussian=cv2.GaussianBlur(img,(3,7),0)
    
    (h, w) = img.shape[:2]
    
    for barcode in decode(img):
        myData= barcode.data.decode('utf-8') #UTF-8 kodlama stilinde, farklı kod birimlerinden meydana gelecek biçimde iki tabanına dönüştürülür. 
        print(myData)
        smaller_frame=cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        
       #çokgen olmasının nedeni kamera olsa bile bir çokgen oluşturabilir.
        pts=np.array([barcode.polygon],np.int32) #
        pts=pts.reshape((-1,1,2))
        cv2.polylines(gaussian, [pts], True, (255,0,255), 3)
        pts2=barcode.rect 
        cv2.putText(gaussian, myData, (pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),1)
        

        pts=np.array([barcode.polygon],np.int32) 
        pts=pts.reshape((-1,1,2))
        cv2.polylines(laplacian, [pts], True, (255,0,255), 3)
        pts2=barcode.rect
        cv2.putText(laplacian, myData, (pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
        
        pts=np.array([barcode.polygon],np.int32) 
        pts=pts.reshape((-1,1,2))
        cv2.polylines(sobel, [pts], True, (255,0,255), 3)
        pts2=barcode.rect
        cv2.putText(sobel, myData, (pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

        pts=np.array([barcode.polygon],np.int32) 
        pts=pts.reshape((-1,1,2))
        cv2.polylines(sobely, [pts], True, (255,0,255), 3)
        pts2=barcode.rect 
        cv2.putText(sobely, myData, (pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

        pts=np.array([barcode.polygon],np.int32) 
        pts=pts.reshape((-1,1,2))
        cv2.polylines(gaussian, [pts], True, (255,0,255), 3)
        pts2=barcode.rect 
        cv2.putText(gaussian, myData, (pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
    
    output= np.zeros((h * 2, w * 2, 3), dtype="uint8")
    output[0:h, 0:w] = gaussian
    output[0:h, w:w * 2] = laplacian
    output[h:h * 2, w:w * 2] = sobel
    output[h:h * 2, 0:w] = sobely
 
    cv2.imshow("out", output)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()