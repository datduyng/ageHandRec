import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='b5913cce90261f910f2548def5058cb30108131c')

# response = visual_recognition.delete_classifier(classifier_id='age_1726438712')
# print(json.dumps(response, indent=2))

# with open('./FinalData/15.zip', 'rb') as file15:
#     updated_model = visual_recognition.update_classifier(
#         classifier_id='age_1813627479',
#         file15_positive_examples=file15)
# print(json.dumps(updated_model, indent=2))

with open('C:/Users/Eric/Desktop/handAgeRecognition/FinalData/1697.png', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.5',
        classifier_ids='age_1176255921')
print(json.dumps(classes, indent=2))

classifiers = visual_recognition.list_classifiers(verbose=True)
print(json.dumps(classifiers, indent=2))