# flask_microservice.py
from flask import Flask, request, jsonify
from transformers import pipeline
from pydantic import BaseModel


app = Flask(__name__)

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    input_data = data.get('input')
    return jsonify(process_data(input_data))

def process_data(input_data):
    """Same function as before"""
    try:
        result = {
            'received': input_data,
            'processed': f"Processed {input_data}",
            'length': len(input_data)
        }
        return {'success': True, 'data': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    input_data = data.get('text')
    return analyze_sentiment(input_data)

def analyze_sentiment(input_data):
    result = sentiment_pipeline(input_data)
    return result
    #return {'success': False, 'error': 'Just a test endpoint'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)