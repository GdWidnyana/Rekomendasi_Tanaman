Sistem Rekomendasi Budidaya Jenis Tanaman Berdasarkan Kondisi Tanah dengan Menggunakan Algoritma Naive Bayes
Mata Kuliah : Pengantar Kecerdasan Buatan

Disusun oleh :
Kelompok III
Kelas C

1.	I Gede Widnyana					(2208561016)
2.	I Gede Widiantara Mega Saputra			(2208561022)
3.	Kadek Belvanatha Gargita Satwikananda	(2208561048)
4.	Putu Yuki Parmawati				(2208561066)
5.	Intara Pratama Harahap				(2208561104)

====================================================

Dalam dunia pertanian, pemilihan jenis tanaman yang tepat untuk ditanam sangatlah vital karena kondisi tanah yang berbeda-beda memengaruhi pertumbuhan dan hasil tan¬aman. Oleh karena itu, sangat penting untuk memperhatikan kondisi tanah dalam memilih jenis tanaman yang akan dibudidayakan. Penelitian ini bertujuan untuk memberikan rekomendasi jenis tanaman yang cocok dibudidayakan berdasarkan data kondisi tanah menggunakan algoritma Naïve Bayes Classifier. Data yang digunakan berjumlah 2201 baris dan 8 kolom yang m diperoleh dari laman kaggle. Pembangunan model dimulai dari tahap pre-processing, analisis data, ekstraksi dan seleksi fitur, implementasi model, validasi model dengan metode K-Fold cross validation, evaluasi model, dan deploy model. Tahap seleksi fitur menggunakan metode Chi-Square untuk memilih fitur yang dapat meningkatkan kinerja model. Tahap validasi model menghasilkan rata-rata skor di angka 99%. Hasil evaluasi model dengan algoritma Gaussian Naïve Bayes direpresentasikan dalam confusion matrix dengan skor accuracy, F1-Score, recall, dan presicion seluruhnya adalah 99% sehingga menunjukkan model memiliki kinerja yang sangat baik. Model tersebut dideploy dalam sebuah webapps dengan framework streamlit untuk memudahkan pengguna dalam mengaksesnya.

====================================================

Link demo : https://c3-sistem-rekomendasi-tanaman.streamlit.app

![image](https://github.com/GdWidnyana/Rekomendasi_Tanaman/assets/120539660/291ace23-11fb-4a03-97c8-8dfbee1acf00)

