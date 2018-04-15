import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version='2016-05-20',
    api_key='b5913cce90261f910f2548def5058cb30108131c'
)

with open('./FinalData/13.zip', 'rb') as file13, open('./FinalData/16.zip','rb') as file16:
    model = visual_recognition.create_classifier(
        'age',
        file13_positive_examples = file13,
        file16_positive_examples = file16
    )


print(json.dumps(model, indent=2))