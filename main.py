from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/api/mesaj")
def mesaj_gonder():
    return {"icerik": "Merhaba! Bu mesaj Render sunucusundan geldi 🚀"}

# Bu kısım sadece bilgisayarında test ederken çalışır.
# Render kendi komutuyla başlatacağı için burası sunucuda çalışmaz, zararı yoktur.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
