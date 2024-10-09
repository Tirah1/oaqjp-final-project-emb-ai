import requests  
import json
def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Access the 'emotion' dictionary inside the first element of the list
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting specific emotion scores
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

     # Returning a dictionary containing emotion score results
    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}
     