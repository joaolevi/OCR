import numpy as np
import cv2

class CndFederalImageProcessing():
    def __init__(self):
        self.image = None
    
    def processamento_img(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
        print(self.image.shape)

    def processar_imagem(self, image):
        image_array = np.array(image)
        self.image = image_array
        try:
            self.processamento_img()
            return self.image
        except Exception as e:
            print("Error processing image. " + str(e))
