"""Package imports"""
from flask import Flask, request, jsonify
import logging
from dotenv import load_dotenv

"""Source imports"""
from src.llm.llama import Llama3
    
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

llm = Llama3(logger)

app = Flask(__name__)

# health
@app.route('/health', methods=['GET'])
def ollama_health():
    return jsonify({'status': 'ok'}), 200

@app.route('/ollama/ocr', methods=['POST'])
def ollama_ocr():
    name_route = 'Rota /ollama/ocr: '
    data = request.get_json()
    if not data or not data['url']:
        logger.info(name_route+'Invalid request data')
        return jsonify({'error': 'Invalid request data'}), 400
    try:
        result_json = llm.vectorization_mode_ocr(data)
        logger.info(name_route+'Document processed successfully: ' + str(result_json))
        return jsonify(result_json), 200
    except Exception as e:
        logger.info(name_route+'Error processing document: ' + str(e))
        return jsonify({'error': str(e)}), 500
    
@app.route('/ollama/dev/ocr', methods=['POST'])
def ollama_ocr_dev():
    name_route = 'Rota /ollama/dev/ocr: '
    data = request.get_json()
    if not data or not data['url']:
        logger.info(name_route+'Invalid request data')
        return jsonify({'error': 'Invalid request data'}), 400
    try:
        result = llm.vectorization_mode_ocr(data)
        logger.info(name_route+'Document processed successfully: ' + str(result))
        return jsonify({"text": result}), 200
    except Exception as e:
        logger.info(name_route+'Error processing document: ' + str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)