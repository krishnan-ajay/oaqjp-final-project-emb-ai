import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze emotion of the given text using IBM Watson NLP service.

    Args:
        text_to_analyze (str): Text to analyze.

    Returns:
        dict: Emotion scores and dominant emotion.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=payload, headers=headers)

    formatted_response = json.loads(response.text)

    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotion_scores["anger"]
    disgust_score = emotion_scores["disgust"]
    fear_score = emotion_scores["fear"]
    joy_score = emotion_scores["joy"]
    sadness_score = emotion_scores["sadness"]

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }


if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))