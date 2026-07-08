# Generated from: preprocessing.ipynb
# Converted at: 2026-07-07T19:31:21.593Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.metrics.distance import edit_distance

# Unduh resource NLTK (Jalankan sekali saja)
nltk.download('punkt')

# ## 1. LOAD DATASET


print("Loading dataset...")
df = pd.read_csv('data/comment_data.csv')
# Kita akan gunakan kolom 'Comment' dan drop missing values jika ada
df = df.dropna(subset=['Comment']).reset_index(drop=True)
print(f"Total data: {len(df)} baris")

# ## 2. FUNGSI REGEX & CLEANING


def clean_text_regex(text):
    # Regex 1: Membersihkan tag HTML (seperti <br>, <a href=>)
    text = re.sub(r'<.*?>', ' ', text)
    
    # Regex 2: Membersihkan URL/Link
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Regex 3: Membersihkan mention (@username) dan hashtag (#)
    text = re.sub(r'\@\w+|\#\w+', '', text)
    
    # Regex 4: Membersihkan tanda baca dan karakter non-alfabet
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Case Folding: Mengubah ke huruf kecil
    text = text.lower()
    
    # Menghapus spasi berlebih
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ## 3. NORMALISASI SLANG & TYPO (Syarat Rubrik: Edit Distance)


# Kamus dinormalisasi sederhana. Pada realitanya bisa dibuat lebih panjang.
slang_dict = {
    'klu': 'kalau', 'gmn': 'bagaimana', 'yg': 'yang', 'd': 'di', 
    'tp': 'tapi', 'maksut': 'maksud', 'gw': 'saya', 'dah': 'sudah',
    'bgt': 'banget', 'bgs': 'bagus', 'mbg': 'makan bergizi gratis'
}

def normalize_text(text):
    words = text.split()
    normalized_words = []
    for word in words:
        # Pengecekan Exact Match ke kamus slang
        if word in slang_dict:
            normalized_words.append(slang_dict[word])
        else:
            normalized_words.append(word)
    return " ".join(normalized_words)

# Contoh penggunaan minimum edit distance
contoh_typo = "nggaran"
target_aspek = "anggaran"
jarak_edit = edit_distance(contoh_typo, target_aspek)
print(f"\n[EVALUASI SIMILARITY] Minimum Edit Distance '{contoh_typo}' ke '{target_aspek}' = {jarak_edit}")

# ## 4. INISIALISASI SASTRAWI & SISTEM CACHING


print("Menyiapkan Stopword dan Stemmer Sastrawi...")
factory_stop = StopWordRemoverFactory()
stopword_remover = factory_stop.create_stop_word_remover()

factory_stem = StemmerFactory()
stemmer = factory_stem.create_stemmer()

# --- INIT CACHING ---
stem_cache = {}

def get_stemmed_word(word):
    # Jika kata belum ada di cache, lakukan stemming dan simpan ke cache
    if word not in stem_cache:
        stem_cache[word] = stemmer.stem(word)
    # Jika sudah ada, langsung ambil dari memori (jauh lebih cepat)
    return stem_cache[word]

# ## 5. PIPELINE PREPROCESSING SUPER CEPAT


def preprocess_pipeline_fast(text):
    # 1. Cleaning & Regex
    text = clean_text_regex(text)
    # 2. Normalisasi Slang
    text = normalize_text(text)
    # 3. Stopword Removal
    text = stopword_remover.remove(text)
    # 4. Stemming dengan Cache
    words = text.split()
    stemmed_words = [get_stemmed_word(w) for w in words]
    return " ".join(stemmed_words)

# Mengaplikasikan ke DataFrame
import time
start_time = time.time()
print("Memulai Preprocessing Pipeline (Menggunakan teknik Caching)...")

df['Clean_Comment'] = df['Comment'].apply(preprocess_pipeline_fast)

end_time = time.time()
print(f"Selesai dalam {end_time - start_time:.2f} detik!\n")

# Menampilkan Tabel Before-After
print("[TABEL BEFORE-AFTER PREPROCESSING]")
display_df = df[['Comment', 'Clean_Comment']].head(5)
print(display_df)

# ## 6. REPRESENTASI TEKS (TF-IDF) & SPARSE REPRESENTATION


print("\nMembuat Representasi TF-IDF...")
vectorizer = TfidfVectorizer(max_features=1500, ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(df['Clean_Comment'])

print(f"Bentuk Matriks TF-IDF: {tfidf_matrix.shape}")
print(f"Matriks adalah 'Sparse', dari {tfidf_matrix.shape[0]} dokumen, terdapat {tfidf_matrix.shape[1]} fitur kata.\n")

# ## 7. COSINE SIMILARITY UNTUK KEMIRIPAN KALIMAT


# 7. COSINE SIMILARITY UNTUK KEMIRIPAN KALIMAT
query = "anggaran program makan gratis terlalu besar"
# Preprocess query agar seragam formatnya dengan dokumen
query_clean = preprocess_pipeline_fast(query)
query_vec = vectorizer.transform([query_clean])

# Menghitung cosine similarity dari query ke seluruh komentar yang sudah bersih
cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
most_similar_idx = cosine_sim.argsort()[-3:][::-1] 

print(f"[COSINE SIMILARITY] Top 3 Komentar mirip dengan query '{query}':")
for idx in most_similar_idx:
    print(f"- Score: {cosine_sim[idx]:.4f} | Teks Asli: {df['Comment'].iloc[idx]}")

# ## 8. MERGE SENTIMENT & STRATIFIED SAMPLING


print("\n[PERSIAPAN DATA ABSA]")
print("Menggabungkan data bersih dengan label sentimen dari Kaggle...")

# Membaca dataset sentimen dari author Kaggle
df_sent = pd.read_csv('/kaggle/input/datasets/dzikriraihan/indonesian-youtube-comments-mbg-program/comment_sentiment.csv')

# Menggabungkan data preprocessing kita (df) dengan kolom sentimen dari Kaggle
# Menggunakan 'Comment ID' sebagai kunci penggabungan agar tidak tertukar
df_final = pd.merge(df, df_sent[['Comment ID', 'Sentiment']], on='Comment ID', how='inner')

print("Melakukan Stratified Sampling untuk mengatasi Class Imbalance...")
# Mengambil sampel acak 150 baris untuk setiap kelas (Negatif, Netral, Positif)
# Total akan menjadi 450 baris data
df_sampled = df_final.groupby('Sentiment').sample(n=150, random_state=42).reset_index(drop=True)

# Menyiapkan kolom kosong untuk kebutuhan anotasi manual (Aspect & NER)
df_sampled['Aspect'] = ""
df_sampled['BIO_Tags'] = ""

# Memilih urutan kolom yang rapi untuk diekspor
kolom_ekspor = ['Comment ID', 'Comment', 'Clean_Comment', 'Aspect', 'Sentiment', 'BIO_Tags']
df_ready = df_sampled[kolom_ekspor]

# Mengekspor ke file CSV baru
output_path = 'absa_dataset_sampled.csv'
df_ready.to_csv(output_path, index=False)

print(f"\nSelesai! Dataset akhir berhasil disimpan sebagai '{output_path}'")
print(f"Distribusi sentimen pada dataset baru:\n{df_ready['Sentiment'].value_counts()}")

from IPython.display import FileLink

# Memunculkan link yang bisa diklik untuk mendownload file
FileLink('absa_dataset_sampled.csv')