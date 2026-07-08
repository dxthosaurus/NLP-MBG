======================================================================
🚀 MODEL: SVM
======================================================================
✅ Model SVM berhasil dilatih dan disimpan ke 'svm_model.joblib'

[1. METRIK EVALUASI]
Accuracy : 0.5889

Classification Report:
              precision    recall  f1-score   support

    negative       0.65      0.73      0.69        30
     neutral       0.54      0.43      0.48        30
    positive       0.56      0.60      0.58        30

    accuracy                           0.59        90
   macro avg       0.58      0.59      0.58        90
weighted avg       0.58      0.59      0.58        90

[3. ERROR ANALYSIS - 5 Contoh Kesalahan Prediksi]
- Aspek       : Umum
  Teks Asli   : Utk ibu hamil dan balita bekerja sama lah dgn bgn posyandu yg sdh mberi mknan tambahan pd balita dan...
  Teks Bersih : utk ibu hamil balita kerja sama lah dgn bgn posyandu sdh mberi mknan tambah pd balita ibu hml
  Aktual      : NEUTRAL | Prediksi : POSITIVE
--------------------------------------------------
- Aspek       : Anggaran
  Teks Asli   : MBG knp tdk memanfaatkan kantin2 sekolah saja, agar tdk terbuang anggaran sewa dapur...
  Teks Bersih : makan gizi gratis knp tdk manfaat kantin sekolah agar tdk buang anggar sewa dapur
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : sampai sekarang menu mbg, pisang / jeruk 1 biji + susu kotak atau ada nasi, tapi tahu tipis, tempe t...
  Teks Bersih : sekarang menu makan gizi gratis pisang jeruk biji susu kotak ada nasi tahu tipis tempe tipis ayam tulang nya gizi nya mana masih gizi makan rumah nya bgn buat aplikasi pantau menu makan gizi gratis guru guru sekolah mengupload foto foton menu sppg terima sekolah sppg nakal di tegur di beri suspend mereka beri menu sesuai porsi
  Aktual      : POSITIVE | Prediksi : NEUTRAL
--------------------------------------------------
- Aspek       : Umum
  Teks Asli   : Ko yg uu tni dan polri gk d bahas pak?...
  Teks Bersih : ko uu tni polri gk bahas pak
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : Yang kerja di  mbg bukan  lah mereka yang membutuhkan  pekerjaan. Melainkan  orang yang berada di se...
  Teks Bersih : kerja makan gizi gratis bukan lah butuh kerja orang yang ada sekitar milik dapur bukan yang miskin
  Aktual      : POSITIVE | Prediksi : NEGATIVE
--------------------------------------------------

======================================================================
🚀 MODEL: RANDOM FOREST
======================================================================
✅ Model Random_Forest berhasil dilatih dan disimpan ke 'random_forest_model.joblib'

[1. METRIK EVALUASI]
Accuracy : 0.6222

Classification Report:
              precision    recall  f1-score   support

    negative       0.63      0.63      0.63        30
     neutral       0.57      0.70      0.63        30
    positive       0.70      0.53      0.60        30

    accuracy                           0.62        90
   macro avg       0.63      0.62      0.62        90
weighted avg       0.63      0.62      0.62        90

[3. ERROR ANALYSIS - 5 Contoh Kesalahan Prediksi]
- Aspek       : Umum
  Teks Asli   : Utk ibu hamil dan balita bekerja sama lah dgn bgn posyandu yg sdh mberi mknan tambahan pd balita dan...
  Teks Bersih : utk ibu hamil balita kerja sama lah dgn bgn posyandu sdh mberi mknan tambah pd balita ibu hml
  Aktual      : NEUTRAL | Prediksi : POSITIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : Alhamdulillah mantap bang  semoga orang2 yg di MBG amanah dalam menjalankn tugasnya.<br>Kasiahan ind...
  Teks Bersih : alhamdulillah mantap bang moga orang di makan gizi gratis amanah menjalankn tugas kasiahan indonesia rakyat nya jt
  Aktual      : POSITIVE | Prediksi : NEUTRAL
--------------------------------------------------
- Aspek       : Anggaran
  Teks Asli   : MBG knp tdk memanfaatkan kantin2 sekolah saja, agar tdk terbuang anggaran sewa dapur...
  Teks Bersih : makan gizi gratis knp tdk manfaat kantin sekolah agar tdk buang anggar sewa dapur
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : sampai sekarang menu mbg, pisang / jeruk 1 biji + susu kotak atau ada nasi, tapi tahu tipis, tempe t...
  Teks Bersih : sekarang menu makan gizi gratis pisang jeruk biji susu kotak ada nasi tahu tipis tempe tipis ayam tulang nya gizi nya mana masih gizi makan rumah nya bgn buat aplikasi pantau menu makan gizi gratis guru guru sekolah mengupload foto foton menu sppg terima sekolah sppg nakal di tegur di beri suspend mereka beri menu sesuai porsi
  Aktual      : POSITIVE | Prediksi : NEUTRAL
--------------------------------------------------
- Aspek       : Anggaran
  Teks Asli   : Mending di kasih bubur kacang hijau tiap seminggu sekali, sisa dana MBG di prioritaskan untuk keseha...
  Teks Bersih : mending kasih bubur kacang hijau tiap minggu sekali sisa dana makan gizi gratis prioritas sehat didik
  Aktual      : NEUTRAL | Prediksi : POSITIVE
--------------------------------------------------

======================================================================
🚀 MODEL: NAIVE BAYES
======================================================================
✅ Model Naive_Bayes berhasil dilatih dan disimpan ke 'naive_bayes_model.joblib'

[1. METRIK EVALUASI]
Accuracy : 0.6111

Classification Report:
              precision    recall  f1-score   support

    negative       0.68      0.77      0.72        30
     neutral       0.57      0.40      0.47        30
    positive       0.57      0.67      0.62        30

    accuracy                           0.61        90
   macro avg       0.61      0.61      0.60        90
weighted avg       0.61      0.61      0.60        90

[3. ERROR ANALYSIS - 5 Contoh Kesalahan Prediksi]
- Aspek       : Umum
  Teks Asli   : Utk ibu hamil dan balita bekerja sama lah dgn bgn posyandu yg sdh mberi mknan tambahan pd balita dan...
  Teks Bersih : utk ibu hamil balita kerja sama lah dgn bgn posyandu sdh mberi mknan tambah pd balita ibu hml
  Aktual      : NEUTRAL | Prediksi : POSITIVE
--------------------------------------------------
- Aspek       : Anggaran
  Teks Asli   : MBG knp tdk memanfaatkan kantin2 sekolah saja, agar tdk terbuang anggaran sewa dapur...
  Teks Bersih : makan gizi gratis knp tdk manfaat kantin sekolah agar tdk buang anggar sewa dapur
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : sampai sekarang menu mbg, pisang / jeruk 1 biji + susu kotak atau ada nasi, tapi tahu tipis, tempe t...
  Teks Bersih : sekarang menu makan gizi gratis pisang jeruk biji susu kotak ada nasi tahu tipis tempe tipis ayam tulang nya gizi nya mana masih gizi makan rumah nya bgn buat aplikasi pantau menu makan gizi gratis guru guru sekolah mengupload foto foton menu sppg terima sekolah sppg nakal di tegur di beri suspend mereka beri menu sesuai porsi
  Aktual      : POSITIVE | Prediksi : NEUTRAL
--------------------------------------------------
- Aspek       : Umum
  Teks Asli   : Ko yg uu tni dan polri gk d bahas pak?...
  Teks Bersih : ko uu tni polri gk bahas pak
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : SEBELUM PENANGKAPAN DADAN, SAYA SANGAT COCOK DG BELIAU, BISA DIALOG DAN MENJELASKAN  DG SEJELAS2NYA,...
  Teks Bersih : tangkap dad sangat cocok dg beliau dialog jelas dg jelas tenang sudah dengar wawancara dad tangkap blm temu wawancara nya masih ragu bukti di temu apa bukti asli dr pak dad dr benci awal suka nanggapin benci makan gizi gratis dengar langsung jelas pak dad biar adem jangan dengar dr benci eeeh pulang dr tanah suci malah di tangkap
  Aktual      : NEGATIVE | Prediksi : NEUTRAL
--------------------------------------------------

======================================================================
🚀 MODEL: LOGISTIC REGRESSION
======================================================================
✅ Model Logistic_Regression berhasil dilatih dan disimpan ke 'logistic_regression_model.joblib'

[1. METRIK EVALUASI]
Accuracy : 0.6000

Classification Report:
              precision    recall  f1-score   support

    negative       0.63      0.73      0.68        30
     neutral       0.57      0.43      0.49        30
    positive       0.59      0.63      0.61        30

    accuracy                           0.60        90
   macro avg       0.60      0.60      0.59        90
weighted avg       0.60      0.60      0.59        90

[3. ERROR ANALYSIS - 5 Contoh Kesalahan Prediksi]
- Aspek       : Umum
  Teks Asli   : Utk ibu hamil dan balita bekerja sama lah dgn bgn posyandu yg sdh mberi mknan tambahan pd balita dan...
  Teks Bersih : utk ibu hamil balita kerja sama lah dgn bgn posyandu sdh mberi mknan tambah pd balita ibu hml
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Anggaran
  Teks Asli   : MBG knp tdk memanfaatkan kantin2 sekolah saja, agar tdk terbuang anggaran sewa dapur...
  Teks Bersih : makan gizi gratis knp tdk manfaat kantin sekolah agar tdk buang anggar sewa dapur
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : sampai sekarang menu mbg, pisang / jeruk 1 biji + susu kotak atau ada nasi, tapi tahu tipis, tempe t...
  Teks Bersih : sekarang menu makan gizi gratis pisang jeruk biji susu kotak ada nasi tahu tipis tempe tipis ayam tulang nya gizi nya mana masih gizi makan rumah nya bgn buat aplikasi pantau menu makan gizi gratis guru guru sekolah mengupload foto foton menu sppg terima sekolah sppg nakal di tegur di beri suspend mereka beri menu sesuai porsi
  Aktual      : POSITIVE | Prediksi : NEUTRAL
--------------------------------------------------
- Aspek       : Umum
  Teks Asli   : Ko yg uu tni dan polri gk d bahas pak?...
  Teks Bersih : ko uu tni polri gk bahas pak
  Aktual      : NEUTRAL | Prediksi : NEGATIVE
--------------------------------------------------
- Aspek       : Menu & Gizi
  Teks Asli   : SEBELUM PENANGKAPAN DADAN, SAYA SANGAT COCOK DG BELIAU, BISA DIALOG DAN MENJELASKAN  DG SEJELAS2NYA,...
  Teks Bersih : tangkap dad sangat cocok dg beliau dialog jelas dg jelas tenang sudah dengar wawancara dad tangkap blm temu wawancara nya masih ragu bukti di temu apa bukti asli dr pak dad dr benci awal suka nanggapin benci makan gizi gratis dengar langsung jelas pak dad biar adem jangan dengar dr benci eeeh pulang dr tanah suci malah di tangkap
  Aktual      : NEGATIVE | Prediksi : POSITIVE
--------------------------------------------------
