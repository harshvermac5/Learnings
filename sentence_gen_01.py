#Defining all the words
subject, verbs, objects = ["I", "You"], ["Play", "Love"], ["Hockey", "Football"]

#Initialising an empty list
sentences = []

for sub in subject:
    for vrb in verbs:
        for obj in objects:
            sentence = f"{sub} {vrb} {obj}"
            sentences.append(sentence)

for sentence in sentences:
    print(sentence)