import cv2
import numpy as np
import pyautogui
import os

# Caricare l'immagine di riferimento
reference_img = cv2.imread(os.path.expanduser("~/Documents/prova/reference.jpg"), cv2.IMREAD_COLOR)



# Acquisire uno screenshot dello schermo
img = pyautogui.screenshot(region=(0,0, 3024, 1964))
frame = np.array(img)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Confrontare l'immagine con l'immagine di riferimento
result = cv2.matchTemplate(frame, reference_img, cv2.TM_CCOEFF_NORMED)
(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
threshold = 0.8 # Soglia di similarità
loc = np.where(result >= threshold)


if len(loc[0]) > 0:
    for pt in zip(*loc[::-1]):
        print("Trovato alle coordinate: x = {}, y = {}".format(pt[0], pt[1]))
        cv2.rectangle(frame, pt, (pt[0] + reference_img.shape[1], pt[1] + reference_img.shape[0]), (0,255,0), 2)

        iniziox = pt[0]
        finex =  reference_img.shape[1]
        mezzox = (pt[0] + pt[0]+reference_img.shape[1])/2

        inizioy = pt[1]
        finey =  reference_img.shape[0]
        mezzoy = (pt[1] + pt[1]+reference_img.shape[0])/2
        x=(mezzox/3600)*1800
        y=(mezzoy/2338)*1169

        pyautogui.moveTo(x, y)
        break
        #print(pyautogui.position())
        #print(pyautogui.size()) #per verificare le dimensioni dello schermo 
        
else:
    print("Non trovato")


"""
# Mostrare l'immagine sullo schermo
cv2.imshow("Screenshot", frame)

# Interrompere il ciclo se si preme il tasto 'q'
cv2.waitKey(0)


cv2.destroyAllWindows()
"""