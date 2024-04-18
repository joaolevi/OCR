import pytesseract
import re
from datetime import datetime

class ExtractTextCRF():
    def __init__(self, image):
        self.image = image
        self.text = None
        self.padrao_cnpj = r'(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
        self.padrao_cnpj_sem_pontos = r'(\d{8}/\d{4}-\d{2})'
        self.padrao_cert_num = r'(\d{22})'
        self.padrao_situacao = r' \b(regular)\b'
        self.padrao_data = r'(\d{2}/\d{2}/\d{4})'

    def verify_cnpj(self):
        cnpj = re.search(self.padrao_cnpj, self.text)
        if cnpj:
            return cnpj.group(0)
        else:
            cnpj = re.search(self.padrao_cnpj_sem_pontos, self.text)
            if cnpj:
                return cnpj.group(0)
            else:
                return None
    
    def verify_cert_num(self):
        cert_num = re.search(self.padrao_cert_num, self.text)
        if cert_num:
            return cert_num.group(0)
        else:
            return None
        
    def verify_situacao(self):
        situacao = re.search(self.padrao_situacao, self.text)
        if situacao:
            return situacao.group(0)
        else:
            return None
        
    def verify_data(self):
        data = re.findall(self.padrao_data, self.text)
        maior_mes = 0
        maior_data = None
        if data:
            for d in data:
                mes = d[3:5]
                if int(mes) > maior_mes:
                    maior_mes = int(mes)
                    maior_data = d
        return maior_data
                
    def verify_all(self):
        cnpj = self.verify_cnpj()
        cert_num = self.verify_cert_num()
        situacao = self.verify_situacao().strip(' ')
        data = self.verify_data()
        
        return cnpj, cert_num, situacao, data
    
    def verify_status(self):
        cnpj, cert_num, situacao, data = self.verify_all()
        if situacao == 'regular' and data >= datetime.now().strftime('%d/%m/%Y'):
            return 'APROVADO', 'Certificado válido'
        elif situacao == 'regular' and data < datetime.now().strftime('%d/%m/%Y'):
            return 'REPROVADO', 'Certificado vencido'
        else:
            return 'REPROVADO', 'Certificado irregular'
    
    def extract_text(self):
        text = ""
        text = pytesseract.image_to_string(self.image, lang='por')
        self.text = text


