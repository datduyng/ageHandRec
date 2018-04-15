import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='b5913cce90261f910f2548def5058cb30108131c')

with open('./FinalData/13yo.png', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        owners= "me")
    print(json.dumps(classes, indent=2))

    