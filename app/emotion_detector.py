import sys
if 'app.emotion_detector' in sys.modules:
    del sys.modules['app.emotion_detector']

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('<your-api-key>')
nlp_service = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
nlp_service.set_service_url('<your-service-url>')

def emotion_predictor(text):
    if not text.strip():
        raise ValueError("Input text cannot be blank.")
    response = nlp_service.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    emotions = response['emotion']['document']['emotion']
    return {k: round(v * 100, 2) for k, v in emotions.items()}
