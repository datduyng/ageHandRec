from watson_developer_cloud import WatsonApiException, VisualRecognitionV3
from socket import *
import json

visual_recognition = VisualRecognitionV3(
    version='2016-05-20',
    api_key='b5913cce90261f910f2548def5058cb30108131c'
)

with open('C:/Users/Eric/Desktop/handAgeRecognition/FinalData/1697.png', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.5',
        classifier_ids='age_1176255921')
print(json.dumps(classes, indent=2))