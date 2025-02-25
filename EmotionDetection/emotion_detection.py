import requests
import json

def emotion_detector(text_to_analyse):
    """
    This functions create a request to the NLP Service and return the response.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_format = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=input_format)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    elif response.status_code  == 400:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
        }
        dominant_emotion = None

    return_format = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
        }
    return return_format



if __name__ == "__main__":
    text = "I love this new technology."
    print(emotion_detector(text))