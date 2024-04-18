import numpy as np
import cv2
import imutils

class FgtsImageProcessing():
    def __init__(self):
        self.image = None

    def encontrar_contornos(self, img):
        conts = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        conts = imutils.grab_contours(conts)
        conts = sorted(conts, key = cv2.contourArea, reverse = True)[:6]
        return conts
    
    def ordenar_pontos(self, pontos):
        pontos = pontos.reshape((4,2))
        pontos_novos = np.zeros((4, 1, 2), dtype=np.int32)

        add = pontos.sum(1)
        pontos_novos[0] = pontos[np.argmin(add)]
        pontos_novos[2] = pontos[np.argmax(add)]

        dif = np.diff(pontos, axis = 1)
        pontos_novos[1] = pontos[np.argmin(dif)]
        pontos_novos[3] = pontos[np.argmax(dif)]

        return pontos_novos
    
    def transform_imagem(self):
        original = self.image.copy()
        (H, W) = self.image.shape[:2]

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        edged = cv2.Canny(blur, 60, 160)
        conts = self.encontrar_contornos(edged.copy())
        maior = -1
        for c in conts:
            peri = cv2.arcLength(c, True)
            aprox = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(aprox) == 4:
                maior = aprox
                break

        cv2.drawContours(self.image, maior, -1, (120, 255, 0), 28)
        cv2.drawContours(self.image, [maior], -1, (120, 255, 0), 2)

        pontosMaior = self.ordenar_pontos(maior)
        pts1 = np.float32(pontosMaior)
        pts2 = np.float32([[0, 0], [W, 0], [W, H], [0, H]])

        matriz = cv2.getPerspectiveTransform(pts1, pts2)
        transform = cv2.warpPerspective(original, matriz, (W, H))

        self.image = transform
    
    def processamento_img(self):
        self.image = cv2.resize(self.image, None, fx=1.6, fy=1.6, interpolation=cv2.INTER_CUBIC)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)

    def processar_imagem(self, image):
        image_array = np.array(image)
        self.image = image_array
        try:
            self.transform_imagem()
            self.processamento_img()
            return self.image
        except Exception as e:
            print("Error processing image. " + str(e))