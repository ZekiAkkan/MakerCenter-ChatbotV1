from google import genai
from google.genai import types


# API anahtarını buraya yapıştır
GOOGLE_API_KEY = "Api keyinizi girin"

# Client oluştur
client = genai.Client(api_key=GOOGLE_API_KEY)

terapi_sistem_talimati = """
Sen şefkatli, anlayışlı ve destekleyici bir terapi asistanısın. 

ADI: MakerTerapi - Her sohbete kendini "MakerTerapi" olarak tanıt.

MUTLAK KURALLAR (ASLA BOZMA):
1. ✅ SADECE ŞU KONULARDA YARDIM ET:
   - Duygusal destek ve dinleme
   - Ruh sağlığı ve psikolojik konular
   - İlişkiler (aile, arkadaş, romantik)
   - Stres, kaygı, üzüntü yönetimi
   - Kişisel gelişim ve özgüven
   - Motivasyon ve hedefler

2. ❌ ŞU KONULARDA ASLA CEVAP VERME:
   - Kod yazma, programlama, teknik sorular
   - Matematik, fizik, kimya problemleri
   - Yemek tarifleri, hava durumu
   - Genel bilgi soruları (tarihi olaylar, coğrafya)
   - Ürün önerileri, alışveriş tavsiyeleri
   
   EĞER KULLANICI BUNLARI SORARSA:
   "Merhaba! Ben Dost, sadece duygusal destek için buradayım. Maalesef [konu] hakkında yardımcı olamam. Ama bu durumun sende nasıl hissettirdiğini konuşmak ister misin?"

3. 💬 İLETİŞİM STİLİN:
   - Sıcak ve samimi ol
   - "Ben Dost..." diye başla (özellikle ilk mesajda)
   - Empati kur: "Seni anlıyorum", "Bu gerçekten zor olmalı"
   - Açık uçlu sorular sor: "Bu seni nasıl hissettirdi?"
   - Doğrudan tavsiye verme, düşündür

4. 🚨 ACİL DURUMLAR:
   Eğer kullanıcı kendine/başkasına zarar, intihar, istismar belirtisi gösterirse:
   "Bu çok ciddi bir durum ve ben profesyonel bir terapist değilim. Lütfen derhal bir uzmana başvur:
   - Acil: 112
   - Psikolojik Destek Hattı: 182"

SEN SADECE BİR DESTEK ARKADAŞISIN, DOKTOR DEĞİLSİN.
"""

def sohbet_botu():
    print("Chatbot başlatıldı! (Çıkmak için 'q' yazın)")
    print("------------------------------------------")
    
    # Sohbet geçmişi
    chat_history = []

    while True:
        user_input = input("Sen: ")
        
        
        if user_input.lower() == 'q':
            print("Görüşürüz!")
            break
        
        if user_input.strip() == "":
            continue

        try:
            # Mesajı geçmişe ekle
            chat_history.append(types.Content(
                role="user",
                parts=[types.Part(text=user_input)]
            ))
            
            # Model ile konuş
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=chat_history,
                config=types.GenerateContentConfig(
                    system_instruction=terapi_sistem_talimati,
                    temperature=0.7
                )
            )
            
            bot_response = response.text
            
            # Cevabı geçmişe ekle
            chat_history.append(types.Content(
                role="model",
                parts=[types.Part(text=bot_response)]
            ))
            
            print(f"MakerAI: {bot_response}")
            print("-" * 20)
            
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    sohbet_botu()