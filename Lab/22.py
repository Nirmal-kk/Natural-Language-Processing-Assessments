import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a sentence: ")

doc = nlp(text)

nouns = []

for token in doc:
    if token.pos_ in ["NOUN", "PROPN"]:
        nouns.append(token.text)

for token in doc:
    if token.pos_ == "PRON":
        if nouns:
            print(token.text, "refers to", nouns[-1])
