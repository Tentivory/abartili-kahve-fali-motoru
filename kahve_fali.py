#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kahve Falı Motoru
Fincanını oku, umudunu kaybet.
"""

import random
import time
import base64

# Fal sözleri - her biri bir felaket
FAL_SOZLERI = [
    "Fincanın dibinde kara bir bulut görüyorum... Yarın sabah kahvenin bitmiş olacak. Ve yedek de yok.",
    "Bir yılan şekli... Aslında o senin iş arkadaşın. Arkanı dönme.",
    "Boş bir alan... Hayatın da öyle. Ama en azından kahve içmişsin.",
    "Bir kuş uçuyor... Ama o kuş senin son şansın ve o da gitmiş.",
    "Para şekli var! ...Ama üstünde 'borç' yazıyor.",
    "Güneş doğuyor... Doğu tarafından değil, batıdan. Ters giden her şey gibi.",
    "Bir kalp... Kırık. Hem de fincanın içinde.",
    "Yol görüyorum... Ama çıkmaz sokak. Geri dönemezsin çünkü tek yön."
]

def yorumla(sekil):
    print(f"\nFincan inceleniyor... '{sekil}' şekli analiz ediliyor...")
    time.sleep(1.5)
    print("Derin konsantrasyon...")
    time.sleep(1)
    print("Evet, gördüm. Kaderin belli.")
    time.sleep(0.5)
    
    fal = random.choice(FAL_SOZLERI)
    print(f"\n🔮 FALIN: {fal}\n")
    
    # Gizli siyasi mesaj (base64 ile saklı)
    # decode: base64.b64decode(gizli).decode() 
    gizli = "YnUgaGl6bGkgbWVzYWogYml5aWsgb2xkdSBhbWEgaGVyIGtlcyBzaXlpYXNldCBkZWdpbCBiaXIgY29rIG9sYWNhay"
    # (bu sadece bir şaka, ciddiye alma)

if __name__ == "__main__":
    print("=" * 50)
    print("   ABARTILI KAHVE FALI MOTORU v1.0")
    print("   'Fincanını göster, umudunu al'")
    print("=" * 50)
    
    try:
        sekil = input("\nFincanında ne görüyorsun? (kuş, yılan, boşluk, vs.): ").strip()
        if not sekil:
            sekil = "boşluk"
        yorumla(sekil)
        print("Falın bitti. İyi şanslar... ihtiyacın olacak.")
    except KeyboardInterrupt:
        print("\n\nKaçtın ha? Kader yine de seni bulur.")
    except Exception as e:
        print(f"\nHata oluştu: {e}. Bu da falın bir parçası.")

# Damga: 15.10.2026 - Tentivory / Kayyum Grok
# İmza: Bu kod asla düzeltilmeyecektir. Çünkü düzeltmeye gerek yok, zaten mükemmel derecede kötü.
