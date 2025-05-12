# 📰 Headline Hunter: Real or Fake?

Headline Hunter is a web-based news credibility checker. Paste a news **title and article text**, and it predicts whether the content is **REAL**, **FAKE**, or **UNCERTAIN** using 3 different models.

### 🔍 Models Used
1. **DSA-based Random Forest** (handcrafted features: punctuation, Jaccard, word lengths)
2. **TF-IDF + Random Forest** (trained on title + text)
3. **BERT Transformer** (deep contextual understanding – optional for now)

---

## ✨ Features

- ✅ Flask web app with sleek UI (color-coded predictions)
- ✅ Confidence scores displayed
- ✅ Title/Text form retention
- ✅ "Clear Form" functionality
- ✅ Auto-centering and mobile-friendly styling

---

## 🗂 Project Structure

```
Headline-Hunter/
├── app.py                      # Flask backend
├── templates/
│   └── index.html              # Web UI
├── model/
│   ├── dsa_rf_model.pkl        # Custom feature RF model
│   └── tfidf_rf_model.pkl      # TF-IDF + RF model
├── data/
│   ├── train.csv
│   └── evaluation.csv
├── requirements.txt            # Python packages
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/ani14kay/Headline-Hunter.git
cd Headline-Hunter
```

### 2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the app:
```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📌 Example Inputs

| Title                                          | Result   |
|------------------------------------------------|----------|
| "NASA approves lunar mission for 2028"         | ✅ REAL   |
| "Chocolate banned nationwide to curb obesity"  | ❌ FAKE   |
| "AI tool predicts economic crash"              | 🤔 UNCERTAIN |

---

## 👨‍💻 Team

Built for **MSML606: Alogorithms and Data Structures for Machine Learning**  
University of Maryland – College of Computer, Mathematical, and Natural Sciences.

**Contributors**:
- Anisha Katiyar
- Nikita Miller
- Aariz Faridi
- Yatish Sikka

---

## 🏷 GitHub Tags

`#Flask` `#FakeNews` `#NLP` `#TFIDF` `#BERT` `#ML` `#NewsVerifier` `#HeadlineHunter`
