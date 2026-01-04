# 🧠 MakerTerapi – Gemini API Tabanlı Terapi Destek Chatbotu


## 🛠️ Kullanılan Teknolojiler

* **Python 3.9+**
* **Google Gemini API**
* `google-generativeai (genai)` Python kütüphanesi

---

## 🔑 Google Gemini API Key Nasıl Alınır?

Aşağıdaki adımları takip ederek ücretsiz bir API anahtarı alabilirsin:

### 1️⃣ Google AI Studio’ya Git

👉 [https://aistudio.google.com/](https://aistudio.google.com/)

### 2️⃣ Google Hesabınla Giriş Yap

### 3️⃣ API Key Oluştur

* **“Create API key”** butonuna tıkla
* Oluşturulan anahtarı kopyala

### 4️⃣ API Key’i Koda Ekle

```python
GOOGLE_API_KEY = "BURAYA_API_KEYİNİ_YAPIŞTIR"
```

## 🧾 Kodun Bölüm Bölüm Açıklaması

### 📌 1. Gerekli Kütüphaneler

```python
from google import genai
from google.genai import types
```

Gemini API ile iletişim kurmak için gerekli modüller içe aktarılır.

---

### 📌 2. API Key ve Client Oluşturma

```python
client = genai.Client(api_key=GOOGLE_API_KEY)
```

Bu satır, Google Gemini servisleriyle iletişimi sağlar.

---

### 📌 3. Sistem Talimatı (En Önemli Kısım)

```python
terapi_sistem_talimati = """
Sen şefkatli, anlayışlı ve destekleyici bir terapi asistanısın.
...
"""
```

Bu talimatlar sayesinde chatbot:

* Sadece **psikolojik destek** konularında konuşur
* Kod, matematik, genel bilgi gibi soruları **reddeder**
* Acil durumlarda **112 ve 182** yönlendirmesi yapar
* Empatik ve yargısız bir dil kullanır

---

### 📌 4. Sohbet Döngüsü

```python
while True:
    user_input = input("Sen: ")
```

* Kullanıcıdan sürekli giriş alınır
* `q` yazılırsa sohbet sonlanır

---

### 📌 5. Gemini’dan Cevap Alma

```python
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=chat_history,
    config=types.GenerateContentConfig(
        system_instruction=terapi_sistem_talimati,
        temperature=0.7
    )
)
```

* `chat_history` sayesinde bağlam korunur
* `temperature=0.7` → doğal ve dengeli cevaplar üretir

---

**MakerTerapi – Yalnız değilsin 🤍**
