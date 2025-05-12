from flask import Flask, render_template, request
import joblib
import heapq
import re
import string
import numpy as np

app = Flask(__name__)
model = joblib.load('model/dsa_rf_model.pkl')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def top_word_freq_ratio(text):
    word_map = {}
    words = text.split()
    for word in words:
        word_map[word] = word_map.get(word, 0) + 1
    return max(word_map.values()) / len(words) if word_map else 0

def top_k_word_lengths(text, k=5):
    words = text.split()
    word_lengths = [len(w) for w in words]
    top_k = heapq.nlargest(k, word_lengths)
    return sum(top_k) / k if top_k else 0

def jaccard_similarity(s1, s2):
    a = set(s1.split())
    b = set(s2.split())
    return len(a & b) / len(a | b) if (a | b) else 0

def punctuation_ratio(text):
    return sum(1 for c in text if c in string.punctuation) / len(text) if text else 0

def capitalization_ratio(text):
    return sum(1 for c in text if c.isupper()) / len(text) if text else 0

def extract_features(title, text):
    clean_title = clean_text(title)
    clean_body = clean_text(text)
    features = [
        top_word_freq_ratio(clean_title),
        top_word_freq_ratio(clean_body),
        top_k_word_lengths(clean_title),
        top_k_word_lengths(clean_body),
        jaccard_similarity(clean_title, clean_body),
        capitalization_ratio(title + " " + text),
        punctuation_ratio(title + " " + text),
        len((title + " " + text).split())
    ]
    return np.array([features])

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    confidence = None
    if request.method == 'POST':
        title = request.form.get('title', '')
        text = request.form.get('text', '')
        features = extract_features(title, text)
        probas = model.predict_proba(features)[0]
        confidence_score = max(probas)
        prediction_label = np.argmax(probas)

        threshold = 0.60  # Minimum confidence required to return label
        if confidence_score >= threshold:
            prediction = 'Real' if prediction_label == 1 else 'Fake'
        else:
            prediction = 'Uncertain'
        confidence = round(confidence_score * 100, 2)

        print("📊 Input features:", features.tolist())
        print("🧠 Model type:", type(model))
        print("➡️ Expected features:", getattr(model, 'n_features_in_', 'Unknown'))

    return render_template('index.html', prediction=prediction, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=False)