"""Emotion Detector Web Application.

This module provides a Flask web application that analyzes user statements
to detect emotions using the emotion_detector function from the EmotionDetection package.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the index page of the web application."""
    return render_template('index.html')


@app.route("/emotionDetector")
def emot_detector():

    """Analyze the given statement and return the emotion scores.

    Returns:
        str: A formatted string with the emotion scores and dominant emotion
             or an error message if the text is invalid.
    """
    # Retrieve the statement to analyze from the request arguments
    text_to_analyze  = request.args.get('textToAnalyze')

    # Call the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)


     # Check if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotion scores and dominant emotion
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
