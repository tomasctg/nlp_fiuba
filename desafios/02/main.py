import re
import os
import string
import PyPDF2

import nltk
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import spacy
import pandas as pd


# ==========================
# 1 — DESCARGAR RECURSOS
# ==========================
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download("omw-1.4")

nlp = spacy.load("en_core_web_sm")


def extract_pdf_text(pdf_path, skip_start=0, skip_end=0):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        total_pages = len(reader.pages)
        
        start = skip_start
        end = total_pages - skip_end
        
        pages = reader.pages[start:end]
        text = "\n".join([
            p.extract_text() for p in pages
            if p.extract_text()
        ])
        
    return text


def segment_sentences(text):
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]


def clean_sentences(sentences):

    patterns_remove_line = [
        r"chapter \d+(\.\d+)*",
        r"section \d+(\.\d+)*",
        r"figure \d+(\.\d+)*",
        r"table \d+(\.\d+)*",
        r"equation \d+(\.\d+)*",
        r"[A-Za-z]+\d+",     # e.g. TCP3, Fig4, eq2
        r"\d+[A-Za-z]+",     # e.g. 3d, 10sec
        r"[ﬀﬁﬃð√∞±≤≥≠≈]"    # caracteres corruptos
    ]

    regex_remove = re.compile("|".join(patterns_remove_line), re.IGNORECASE)

    cleaned = []
    for s in sentences:
        original = s
        s = regex_remove.sub(" ", s)
        s = re.sub(r'\s+', ' ', s).strip()

        if len(s) < 3:
            continue

        cleaned.append(s)

    return cleaned


def nltk_process_sentence(sentence, stop_words, lemmatizer):

    tokens = word_tokenize(sentence)

    lemmas = [lemmatizer.lemmatize(w.lower()) for w in tokens]

    no_punct = [w for w in lemmas if w not in string.punctuation]

    no_stop = [w for w in no_punct if w not in stop_words]

    return no_stop


def preprocess_all(sentences):

    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    processed = []
    for s in sentences:
        clean_tokens = nltk_process_sentence(s, stop_words, lemmatizer)
        if clean_tokens:
            processed.append(clean_tokens)

    return processed


def is_pure_text(tokens):

    text = " ".join(tokens)

    # no números
    if re.search(r"\d", text):
        return False

    # no illustraciones
    if re.search(r"\billustrat\w*\b", text, re.IGNORECASE):
        return False

    # no figuras, tablas, diagramas
    if re.search(r"\b(fig|figure|table|diagram)\b", text, re.IGNORECASE):
        return False

    return True


def filter_pure_text(sentences):
    return [s for s in sentences if is_pure_text(s)]


TCP_PATTERN = re.compile(
    r"\bTCP\b|\bTCP/IP\b|\bTransmission Control Protocol\b|\bTCP-based\b|\btcp\b",
    re.IGNORECASE
)

def filter_tcp(sentences):
    tcp_sents = []
    for tokens in sentences:
        if TCP_PATTERN.search(" ".join(tokens)):
            tcp_sents.append(tokens)
    return tcp_sents


def process_pdf(pdf_path, skip_start=12, skip_end=7):

    print("Extrayendo texto...")
    raw_text = extract_pdf_text(pdf_path, skip_start, skip_end)

    print("Segmentando oraciones...")
    segmented = segment_sentences(raw_text)

    print("Limpieza regex...")
    cleaned = clean_sentences(segmented)

    print("Preprocesando NLTK...")
    processed = preprocess_all(cleaned)

    print("Filtrando PURE TEXT...")
    pure_text = filter_pure_text(processed)

    print("Extrayendo solo TCP...")
    tcp_only = filter_tcp(pure_text)

    print(f"Total sentencias TCP limpias: {len(tcp_only)}")
    return tcp_only


if __name__ == "__main__":
    result = process_pdf("internet_congestion.pdf")

    with open("tcp_corpus_clean.txt", "w", encoding="utf-8") as f:
        for sent in result:
            f.write(" ".join(sent) + "\n")

    print("\nArchivo final generado: tcp_corpus_clean.txt")
