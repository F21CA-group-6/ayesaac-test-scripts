import re
import json

def extract_label(text):
    patterns = [
        "ingredients",
        "allergens"
    ]

    # make text lowercase and remove most special characters
    text = re.sub('\s+\n', ' ', text).lower()
    text = re.sub('[^a-z0-9() ]+', '', text)
    text = [text]
    regex = '(^.*ingredients|allergens)'
    text = re.split(regex, text[0])
    data = {}
    print(text)
    max_len = -1
    likely_string = None
    for pattern in patterns:
        likely_string = ""
        for i in range(len(text)):
            if (text[i] != ''):
                if (text[i] == pattern):
                    next_string = text[i+1]
                    cur_len = len(next_string)

                    # Assume that the longest string after pattern is the one
                    if (cur_len > max_len):
                        max_len = cur_len
                        likely_string = next_string
                data[pattern] = likely_string

    json_string = json.dumps(data)
    print(json_string)
    return json_string

label_text = ""
with open("label.txt") as f:
    label_text = f.read()

with open("out.json", "w+") as f:
    formatted_label_text = extract_label(label_text)
    f.write(formatted_label_text)
