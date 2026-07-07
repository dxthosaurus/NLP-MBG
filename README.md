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
│   ├── preprocessing.ipynb              # Script pembersihan data & similarity
│   ├── train_model.ipynb                # Script pelatihan 4 model klasifikasi (ABSA)
│   └── train_ner.ipynb                  # Script ekstraksi dan evaluasi NER
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

**2. Buat Virtual Environment**
* Sangat disarankan menggunakan virtual environment agar versi library tidak bentrok dengan proyek Python lainnya.

**3. Aktifkan Virtual Environment**
* .\venv\Scripts\Activate.ps1
(Catatan: Jika terjadi error Execution_Policies, jalankan perintah Set-ExecutionPolicy Unrestricted -Scope CurrentUser terlebih dahulu sebagai Administrator).

**4. Instal Dependensi**
* pip install -r requirements.txt

---

## 🚀 Cara Pelatihan Ulang Model (Training)
Jika Anda ingin melatih ulang model dengan dataset yang baru, jalankan script yang tersedia di dalam folder notebooks/. Eksekusi dilakukan dari direktori utama (root).

**1. Melakukan preprocessing data**
* python notebooks/preprocessing.ipynb
Script ini akan memuat dataset dan melakukan preprocessing pada data. Notebook ini akan memanggil dataset **comment_data.csv** dan dataset **comment_sentiment.csv**, pastikan jalur direktorinya sudah benar. Kemudian notebook ini akan menghasilkan **absa_dataset_sampled.csv** yang nanti digunakan pada step 2 dan 3.

**2. Melatih Model Klasifikasi ABSA**
* python notebooks/train_model.ipynb
Script ini akan memuat dataset, mengekstraksi TF-IDF, melatih 4 algoritma, menampilkan Confusion Matrix, dan menyimpan model .joblib ke folder models/.

**3. Melatih dan Mengevaluasi NER
* python notebooks/train_ner.py
Script ini akan menjalankan Rule-Based NER dan melakukan simulasi evaluasi pencetakan matriks presisi level-token.

---

## 🌐 Cara Menjalankan Aplikasi Web (Deployment Lokal)
Aplikasi web interaktif digunakan untuk melakukan inferensi (testing) kalimat baru secara langsung tanpa perlu proses training ulang, menggunakan arsitektur caching memori.

Jalankan perintah berikut di terminal:
* streamlit run app.py

Aplikasi akan otomatis terbuka di browser bawaan pada alamat lokal http://localhost:8501.

💡 Contoh Penggunaan Aplikasi
1. Buka aplikasi web yang telah berjalan di browser Anda.

2. Pada area input teks, masukkan contoh opini masyarakat:

"Menu nya sedikit banget, terus ini anggarannya nyampe ga... atau disunat? gila emang"

3. Klik tombol Analisis dengan 4 Model.

4. Hasil Output:

NER Ekstraksi: Kata Menu dan anggarannya akan disorot dengan warna kuning (menandakan deteksi entitas ASPECT).

Dashboard Probabilitas: Keempat model (SVM, Random Forest, Naive Bayes, Logistic Regression) akan menampilkan progress bar, di mana secara mayoritas akan menunjuk probabilitas tertinggi pada kelas NEGATIF.

Proyek Akademik Ujian Akhir Semester (UAS) - Pemrosesan Bahasa Alami | Universitas Dian Nuswantoro (2026)
