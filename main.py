from fastapi import FastAPI
from fastapi.responses import StreamingResponse # Resim verisi göndermek için gerekli
import uvicorn
import matplotlib.pyplot as plt
import numpy as np
import io # Hafızada dosya işlemleri için

app = FastAPI()

@app.get("/api/grafik")
def grafik_olustur():
    # 1. Verileri Hazırla
    # -10 ile +10 arasında 100 tane eşit aralıklı sayı üret (X ekseni için)
    x = np.linspace(-10, 10, 100)
    # Fonksiyonu uygula: y = x^2 + 3
    y = x**2 + 3

    # 2. Grafiği Çiz (Nesne tabanlı yaklaşım - sunucular için daha güvenli)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='y = x^2 + 3', color='blue')
    
    # Grafiği süsle
    ax.set_title("İkinci Dereceden Fonksiyon Grafiği")
    ax.set_xlabel("X Ekseni")
    ax.set_ylabel("Y Ekseni")
    ax.grid(True) # Izgara ekle
    ax.legend() # Lejantı göster

    # 3. Grafiği Hafızaya Kaydet (Diske değil!)
    # 'buf' adında hafızada bir bayt tamponu (sanal dosya) oluşturuyoruz.
    buf = io.BytesIO()
    # Çizdiğimiz figürü bu tampona PNG formatında kaydediyoruz.
    fig.savefig(buf, format="png")
    # Tamponun başına geri sarıyoruz (okumaya baştan başlamak için).
    buf.seek(0)
    
    # Hafızayı temizle (sonraki istekler için önemli)
    plt.close(fig)

    # 4. Resmi Yanıt Olarak Gönder
    # StreamingResponse, dosya benzeri nesneleri (buf) HTTP yanıtı olarak gönderir.
    # media_type="image/png" diyerek karşı tarafa bunun bir PNG resmi olduğunu söylüyoruz.
    return StreamingResponse(buf, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
