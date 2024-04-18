from flask import Flask, request, jsonify
from extractors.extract_text_crf import ExtractTextCRF as CRF
from extractors.extract_text_cndf import ExtractTextCNDF as CNDF
from document_recognizer import DocumentRecognizer
from pdf2image import convert_from_bytes
import logging
from imageprocessing.fgts_processing import FgtsImageProcessing
from imageprocessing.cndf_processing import CndFederalImageProcessing

FGTS = 'Certidão Regularidade - FGTS'
CERTIDAO_DEBITO_FEDERAL = 'Certidão Débito - Tributos Federais (Receita Federal)'

app = Flask(__name__)

ml_model = DocumentRecognizer('models/document_type_recognizer_v1.0.0.pkl')
fgts_processing = FgtsImageProcessing()
cndf_processing = CndFederalImageProcessing()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Nenhum arquivo enviado', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400
    
    if file and file.filename.endswith('.pdf'):
        pdf = file.read()
        images = convert_from_bytes(pdf)
        document_type = ml_model.predict(images[0])
        print('Documento enviado é uma ' + document_type)
        if document_type == FGTS:
            imagem_processada = fgts_processing.processar_imagem(images[0])
            crf = CRF(imagem_processada)
            crf.extract_text()
            cnpj, cert_num, situacao, data = crf.verify_all()
            status_aprovacao, motivo = crf.verify_status()
            return jsonify({
                "status_aprovacao": status_aprovacao,
                "cnpj": cnpj,
                "cert_num": cert_num,
                "situacao": situacao,
                "data_vencimento_certificado": data,
                "motivo": motivo,
                "tipo_documento": document_type
            }), 200
        elif document_type == CERTIDAO_DEBITO_FEDERAL:
            imagem_processada = cndf_processing.processar_imagem(images[0])
            print(type(imagem_processada))
            cndf = CNDF(imagem_processada)
            cndf.extract_text()
            cnpj, cert_num, situacao, data = cndf.verify_all()
            status_aprovacao, motivo = cndf.verify_status()
            return jsonify({
                "status_aprovacao": status_aprovacao,
                "cnpj": cnpj,
                "cert_num": cert_num,
                "situacao": situacao,
                "data_vencimento_certificado": data,
                "motivo": motivo,
                "tipo_documento": document_type
            }), 200
        else:
            return 'O documento enviado não é uma Certidão Regularidade - FGTS', 400
    else:
        return 'O arquivo enviado não é um PDF', 400

if __name__ == '__main__':
    app.run(debug=True)
