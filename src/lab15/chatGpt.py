import openai
from sentence_transformers import SentenceTransformer
import numpy as np
import spacy
from scipy.spatial.distance import cosine
nlp = spacy.load("en_core_web_sm")
openai.api_key = "MY SECRET KEY"

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def ask_chatgpt(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{question}\n- ChatGPT: ",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].text.strip()

def sentence_similarity(sent1, sent2):
    emb1 = model.encode([sent1])
    emb2 = model.encode([sent2])
    return 1 - cosine(emb1, emb2)

# Split text into sentences
def split_sentences(text):
    doc = nlp(text)
    return [str(sent) for sent in doc.sents]

# Calculate similarity between two texts
def similarity(text1, text2):
    """
    The metric calculates the average cosine similarity between corresponding sentences
    in the two texts. If one text has more sentences, it only considers the common number
    of sentences in both texts.
    """
    sentences1 = split_sentences(text1)
    sentences2 = split_sentences(text2)

    similarities = [
        sentence_similarity(s1, s2)
        for s1, s2 in zip(sentences1, sentences2)
    ]

    return np.mean(similarities)

# Ask a question
question = "How are you today?"
response1 = ask_chatgpt(question)

# Regenerate the response
response2 = ask_chatgpt(question)

# Calculate similarity
similarity = similarity(response1, response2)

print(f"Response 1:\n{response1}")
print(f"Response 2:\n{response2}")
print(f"Overall similarity: {similarity}")
