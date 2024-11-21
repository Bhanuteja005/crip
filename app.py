# app.py
from flask import Flask, render_template, jsonify
from crypto_analyzer import fetch_top_cryptocurrencies, analyze_cryptocurrency_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/crypto-data')
def get_crypto_data():
    df = fetch_top_cryptocurrencies()
    if df is not None:
        analysis = analyze_cryptocurrency_data(df)
        return jsonify({
            'data': df.to_dict('records'),
            'analysis': analysis
        })
    return jsonify({'error': 'Failed to fetch data'})

if __name__ == '__main__':
    app.run(debug=True)