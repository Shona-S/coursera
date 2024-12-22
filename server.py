"""
This is the main server file for the Emotion Detection Application.
It uses Flask to create an API that predicts emotions based on text input.
"""

from flask import Flask, request, jsonify
from app import emotion_predictor

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict_emotion():
    """
    This endpoint receives text as input and returns the predicted emotions.
    It expects a JSON payload with the 'text' field and returns the emotion analysis.
    """
    try:
        data = request.json
        text = data.get("text", "")
        result = emotion_predictor(text)
        return jsonify({"success": True, "emotions": result})
    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400

@app.errorhandler(ValueError)
def handle_value_error():
    """
    Handles ValueErrors and returns a JSON response with the error message.
    """
    return jsonify({"success": False, "error": "Invalid input provided."}), 400

if __name__ == "__main__":
    app.run(debug=True)
