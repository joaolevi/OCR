import joblib
import numpy as np
import cv2
import logging

class_name = 'DocumentRecognizer.'

class DocumentRecognizer():
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.classes = [
            'Certidão Regularidade - FGTS',
            'Certidão Débito - Tributos Federais (Receita Federal)'
        ]
    
    def predict(self, image):
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        logging.info(f'{class_name}Predicting document type')
        logging.info(f'{class_name}Image shape: {image.shape}')
        image = cv2.resize(image, (100, 100))
        features = image.flatten()
        prediction = self.model.predict([features])
        return prediction[0]
    
