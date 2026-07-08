# Generated from: train_model.ipynb
# Converted at: 2026-07-07T19:30:33.489Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import sklearn
print(sklearn.__version__)

# ### 1. LOAD DATA & AUTO-FILL ASPECT


print("Loading dataset hasil koreksi...")
df = pd.read_csv('data/absa_dataset_sampled.csv')

aspect_keywords = {
    'Anggaran': ['anggaran', 'dana', 'uang', 'pajak', 'korupsi', 'triliun', 'biaya'],
    'Menu & Gizi': ['menu', 'susu', 'makan', 'gizi', 'nasi', 'lauk', 'sayur', 'telur'],
    'Distribusi': ['distribusi', 'sekolah', 'daerah', 'papua', 'desa', 'merata', 'tepat sasaran'],
    'Pemerintah': ['pemerintah', 'prabowo', 'gibran', 'menteri', 'kebijakan', 'program']
}

def detect_aspect(text):
    text_lower = str(text).lower()
    for aspect, keywords in aspect_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return aspect
    return 'Umum'

df['Aspect'] = df['Clean_Comment'].apply(detect_aspect)

# ### 2. FITUR TF-IDF, CEK DISTRIBUSI, & SPLIT DATA


df['Clean_Comment'] = df['Clean_Comment'].fillna("")
df['Aspect'] = df['Aspect'].fillna("Umum")
df['Feature_Text'] = df['Aspect'] + " " + df['Clean_Comment']

vectorizer = TfidfVectorizer(max_features=1500, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['Feature_Text'])
y = df['Sentiment']

joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')
print("✅ Vectorizer disimpan ke 'models/tfidf_vectorizer.joblib'")

print("\n[INFO DATASET SEBELUM SPLIT]")
print(f"Total data siap training: {len(df)} baris")
print("Distribusi Kelas Sentimen Aktual:")
print(y.value_counts())
print("-" * 50)

X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(
    X, y, df.index, test_size=0.2, random_state=42, stratify=y
)

# ### 3. TRAINING, EVALUASI, & VISUALISASI PER MODEL


models = {
    "SVM": SVC(kernel='linear', C=1.0, random_state=42, probability=True),
    "Random_Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Naive_Bayes": MultinomialNB(),
    "Logistic_Regression": LogisticRegression(max_iter=1000, random_state=42)
}

test_df_base = df.iloc[indices_test].copy()

# Mengatur style visual Seaborn agar elegan
sns.set_theme(style="whitegrid", font_scale=1.1)

for name, model in models.items():
    print("\n" + "="*70)
    print(f"🚀 MODEL: {name.replace('_', ' ').upper()}")
    print("="*70)
    
    # Training Model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Export model ke .joblib
    filename = f"{name.lower()}_model.joblib"
    joblib.dump(model, filename)
    
    print(f"✅ Model {name} berhasil dilatih dan disimpan ke '{filename}'")
# --- A. METRIK EVALUASI ---
    print(f"\n[1. METRIK EVALUASI]")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
# --- B. VISUALISASI CONFUSION MATRIX ---
    print("\n[2. CONFUSION MATRIX]")
    cm = confusion_matrix(y_test, y_pred, labels=['negative', 'neutral', 'positive'])
    
    # Membuat figure matplotlib
    plt.figure(figsize=(7, 5))
    
    # Menggambar Heatmap menggunakan Seaborn
    # cmap='Blues' memberikan gradasi warna biru yang profesional
    ax = sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', linewidths=1, linecolor='white',
                     xticklabels=['Negatif', 'Netral', 'Positif'],
                     yticklabels=['Negatif', 'Netral', 'Positif'])
    
    plt.title(f'Confusion Matrix - {name.replace("_", " ")}', fontsize=14, pad=15, fontweight='bold')
    plt.xlabel('Prediksi Model', fontsize=12, labelpad=10)
    plt.ylabel('Aktual (Ground Truth)', fontsize=12, labelpad=10)
    plt.tight_layout()
    
    # Menampilkan confusion matrix
    plt.show()
    
# --- C. ERROR ANALYSIS ---
    print("\n[3. ERROR ANALYSIS - 5 Contoh Kesalahan Prediksi]")
    test_df = test_df_base.copy()
    test_df['Predicted_Sentiment'] = y_pred
    
    errors = test_df[test_df['Sentiment'] != test_df['Predicted_Sentiment']].head(5)
    
    if len(errors) == 0:
        print("Hebat! Model ini memprediksi seluruh 5 data teratas dengan benar.")
    else:
        for i, row in errors.iterrows():
            print(f"- Aspek       : {row['Aspect']}")
            print(f"  Teks Asli   : {row['Comment'][:100]}...") 
            print(f"  Teks Bersih : {row['Clean_Comment']}")
            print(f"  Aktual      : {row['Sentiment'].upper()} | Prediksi : {row['Predicted_Sentiment'].upper()}")
            print("-" * 50)

print("\n🎉 EKSPERIMEN MULTI-MODEL & VISUALISASI SELESAI!")