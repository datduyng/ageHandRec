## compute_input.py

import sys, json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version='2016-05-20',
    api_key='b5913cce90261f910f2548def5058cb30108131c'
)

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()

    with open(lines, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.5',
            classifier_ids='age_1176255921')
    #create a numpy array
    #np_lines = np.array(lines)

    #use numpys sum method to find sum of all elements in the array
    #lines_sum = np.sum(np_lines)

    #return the sum to the output stream
    print(classes)

#start process
if __name__ == '__main__':
    main()