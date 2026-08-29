from nltk.corpus import wordnet as wn

word = input("Enter a word: ")

synsets = wn.synsets(word)

for syn in synsets:
    print("\nSynset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print("Lemmas:", syn.lemma_names())