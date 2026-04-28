import requests


def dizi_asistani():
    print("--- Dizi Takip Sistemi (TVmaze) ---")
    dizi_adi = input("Takip etmek istediğiniz dizinin adını yazın: ").strip()

    # API Key gerektirmez!
    url = f"https://api.tvmaze.com/singlesearch/shows?q={dizi_adi}&embed=episodes"

    try:
        cevap = requests.get(url)
        if cevap.status_code == 200:
            veri = cevap.json()

            print(f"\n📺 Dizi: {veri['name']}")
            print(f"⭐ Puan: {veri['rating']['average']}")
            print(f"📅 Durum: {veri['status']}")
            print(f"🎭 Türler: {', '.join(veri['genres'])}")

            # Son bölüm bilgisini çekme
            bolumler = veri['_embedded']['episodes']
            if bolumler:
                son_bolum = bolumler[-1]
                print(f"🏁 Son Yayınlanan Bölüm: S{son_bolum['season']}E{son_bolum['number']} - {son_bolum['name']}")
        else:
            print("Dizi bulunamadı.")

    except Exception as e:
        print(f"Hata: {e}")


if __name__ == "__main__":
    dizi_asistani()
