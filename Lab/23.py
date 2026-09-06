from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter a text: ")

sentences = text.split(".")

sentences = [s.strip() for s in sentences if s.strip()]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)

score = 0

for i in range(len(sentences) - 1):
    similarity = cosine_similarity(vectors[i], vectors[i + 1])[0][0]
    score += similarity
    print("Similarity:", round(similarity, 2))

if len(sentences) > 1:
    coherence = score / (len(sentences) - 1)
else:
    coherence = 1

print("Coherence Score:", round(coherence, 2))

if coherence > 0.3:
    print("The text is coherent.")
else:
    print("The text is not very coherent.")
