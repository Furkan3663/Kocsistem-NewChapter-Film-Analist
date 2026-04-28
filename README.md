Bu Proje kullanıcıların merak ettiği film ve diziler hakkında güncel verilere hızlıca ulaşmasını sağlayan, Python tabanlı bir backend projesidir. Bu çalışma, **KoçSistem NewChapter** teknik değerlendirme süreci kapsamında geliştirilmiştir.

## 🚀 Proje Amacı
Bu projenin temel amacı, karmaşık film veri tabanlarından gelen ham verileri (JSON) anlamlı bir yapıya dönüştürerek kullanıcıya sunmaktır. Sistem, temiz kod (clean code) prensipleriyle yazılmış olup, ileride **GenAI (Üretken Yapay Zeka)** modelleri ile derinlemesine analiz yapabilecek şekilde genişletilmeye müsait bir mimariye sahiptir.

## 🛠️ Kullanılan Teknolojiler
* **Programlama Dili:** Python 3.10+
* **Veri Kaynağı:** TVmaze REST API (Dinamik veri çekimi için)
* **Kütüphaneler:** `requests` (HTTP protokol yönetimi)

## 📋 Öne Çıkan Özellikler
* **Dinamik Arama:** Kullanıcı girdilerine göre anlık API sorgulaması.
* **Veri İşleme:** Ham HTML verilerinin temizlenerek kullanıcı dostu metne dönüştürülmesi.
* **Hata Yönetimi:** Geçersiz sorgular veya bağlantı hataları için geliştirilmiş kontrol mekanizmaları.
* **Modüler Yapı:** Kolay okunabilir ve geliştirilebilir fonksiyonel tasarım.

## ⚙️ Kurulum ve Çalıştırma
Projeyi yerel bilgisayarınızda test etmek için:

1. Depoyu klonlayın:
   `git clone [GITHUB_REPO_LINKINIZ]`
2. Gerekli kütüphaneyi yükleyin:
   `pip install requests`
3. Uygulamayı başlatın:
   `python main.py`

---
**Geliştirici:** [Furkan Arslan]  
**Tarih:** 28 Nisan 2026
