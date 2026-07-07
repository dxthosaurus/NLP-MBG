# NLP-MBG
# 🍽️ Analisis Sentimen & NER Program Makan Bergizi Gratis (MBG)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)

Repositori ini berisi proyek **Pemrosesan Bahasa Alami (NLP)** untuk menganalisis opini publik terkait kebijakan Makan Bergizi Gratis (MBG) di Indonesia berdasarkan data komentar YouTube. Proyek ini menggabungkan arsitektur *Aspect-Based Sentiment Analysis* (ABSA) menggunakan pendekatan komparasi Multi-Model dan *Named Entity Recognition* (NER) berbasis aturan (*Rule-Based*).

---

## ✨ Fitur Utama & Arsitektur
* **Rule-Based NER & BIO Tagging:** Mengekstrak entitas spesifik seperti Aspek (Menu, Anggaran), Tokoh, Organisasi, dan Lokasi secara *real-time* menggunakan pencocokan kamus.
* **Preprocessing & TF-IDF Bigram:** Pembersihan teks tingkat lanjut (Regex, Normalisasi Typo dengan *Minimum Edit Distance*, Sastrawi Stemming) dan ekstraksi fitur kata menggunakan matriks TF-IDF berpasangan (N-Gram).
* **Pseudo-ABSA Pipeline:** Memanfaatkan injeksi konteks (*text concatenation*) dari aspek yang terdeteksi untuk mengarahkan pembobotan atensi fitur sentimen.
* **Multi-Model Inference:** Membandingkan performa 4 algoritma klasifikasi *Machine Learning* secara paralel (Random Forest, SVM, Naive Bayes, Logistic Regression).
* **Interactive Dashboard:** Antarmuka web dibangun dengan Streamlit, dilengkapi penyorotan teks dinamis (*NER Highlighting*) dan visualisasi tingkat probabilitas model.

## 📊 Hasil Evaluasi
Dataset yang digunakan merupakan data dunia nyata (*in-the-wild*) tanpa kurasi label manual, berjumlah 450 baris melalui *stratified sampling*. Evaluasi klasifikasi sentimen membuktikan bahwa model *ensemble* lebih tangguh terhadap *noise label*:
1. **Random Forest Classifier:** 62.22% 🏆 *(Terbaik)*
2. **Multinomial Naive Bayes:** 61.11%
3. **Logistic Regression:** 60.00%
4. **Support Vector Machine (Linear):** 58.89%

---

## 📂 Struktur Direktori

```text
nlp-mbg-project/
│
├── app/
|   ├── streamlit_app.py                 # File utama aplikasi Streamlit
|   ├── requirements.txt                 # Dependensi yang dibutuhkan aplikasi
|
├── data/
│   ├── absa_dataset_sampled.csv         # Dataset label sentimen & aspek (450 baris)
│   └── ner_bio_dataset.tsv              # Dataset token-level format BIO Tagging
│
├── models/
│   ├── tfidf_vectorizer.joblib          # Model ekstraksi fitur TF-IDF Bigram
│   ├── random_forest_model.joblib       # Model Random Forest Classifier
│   ├── svm_model.joblib                 # Model Support Vector Machine (Linear)
│   ├── naive_bayes_model.joblib         # Model Multinomial Naive Bayes
│   └── logistic_regression_model.joblib # Model Logistic Regression
│
├── notebooks/
│   ├── preprocessing.py                 # Script pembersihan data & similarity
│   ├── train_model.py                   # Script pelatihan 4 model klasifikasi (ABSA)
│   └── train_ner.py                     # Script ekstraksi dan evaluasi NER
│
├── requirements.txt                     # Daftar library dependensi
└── README.md                            # Dokumentasi repositori

```
---
## ⚙️ Panduan Instalasi (Windows / VS Code)
Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda menggunakan terminal PowerShell/CMD di Visual Studio Code.

**1. Clone repositori ini**
* git clone [https://github.com/username-github-anda/nlp-mbg-project.git](https://github.com/username-github-anda/nlp-mbg-project.git)
cd nlp-mbg-project

2. Buat Virtual Environment
* Sangat disarankan menggunakan virtual environment agar versi library tidak bentrok dengan proyek Python lainnya.

**3. Aktifkan Virtual Environment**
* .\venv\Scripts\Activate.ps1
(Catatan: Jika terjadi error Execution_Policies, jalankan perintah Set-ExecutionPolicy Unrestricted -Scope CurrentUser terlebih dahulu sebagai Administrator).

**4. Instal Dependensi
* pip install -r requirements.txt

## 🚀 Cara Pelatihan Ulang Model (Training)
Jika Anda ingin melatih ulang model dengan dataset yang baru, jalankan script yang tersedia di dalam folder notebooks/. Eksekusi dilakukan dari direktori utama (root).
**1. Melatih Model Klasifikasi ABSA
* python notebooks/train_model.py
