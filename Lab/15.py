import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.5]
NP -> 'John' [0.5]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'cat' [0.5]
N -> 'dog' [0.5]
V -> 'sees' [1.0]
""")

sentence = input("Enter sentence: ").split()

parser = ViterbiParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.probability())