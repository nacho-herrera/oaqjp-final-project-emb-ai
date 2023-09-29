""" 
This program spin up a webserver that recieve 
a sentence and runs a emotion detecting algorithm
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detection():
    """ 
    This code receives the text from the HTML page, and 
    runs sentiment analysis using the emotion_detector 
    function. The output is passed to the webpage as response
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "invalid input! "
    return f"""For the given statement, the system response is
     'anger': {response['anger']},
     'disgust': {response['disgust']},
     'fear': {response['fear']},
     'joy': {response['joy']}
     and 'sadness': {response['sadness']},
     The dominant emotion is {response['dominant_emotion']}."""

@app.route('/')
def index():
    """Index of the webpage""" 

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
