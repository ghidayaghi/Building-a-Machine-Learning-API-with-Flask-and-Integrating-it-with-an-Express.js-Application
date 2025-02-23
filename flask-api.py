from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Invalid input. Provide a 'text' field."}), 400
        
        text = data['text']
        
        sentiment_scores = analyzer.polarity_scores(text)
        
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            sentiment = "positive"
        elif compound_score <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return jsonify({"sentiment": sentiment})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
