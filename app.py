import streamlit as st
from collections import Counter
import re
import os

st.title("NLP N-gram Analyzer")

BASE_DIR = os.path.dirname(__file__)

@st.cache_data
def load_corpus():
    with open(os.path.join(BASE_DIR, "corpus.txt"), "r", encoding="utf-8") as f:
        text = f.read().lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.split()

words = load_corpus()

n = st.slider("Select N-gram size", 1, 5, 2)

ngrams = zip(*[words[i:] for i in range(n)])
ngram_freq = Counter(ngrams)

st.subheader(f"Top 20 {n}-grams")
for gram, freq in ngram_freq.most_common(20):
    st.write(" ".join(gram), "→", freq)
