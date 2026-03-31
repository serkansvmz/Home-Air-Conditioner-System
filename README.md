# Home-Air-Conditioner-System
Bu proje, PIC16F877A mikrodenetleyici tabanlı bir ev tipi klima/ısı kontrol sistemi ile Python üzerinden seri haberleşme arayüzünü içermektedir.

## Sistem:
  - **Ortam sıcaklığını ölçer**
  - **Kullanıcıdan hedef sıcaklık alır**
  - **Fan hızını ölçer**
  - **Isıtma / soğutma kontrolü yapar**
  - **UART üzerinden PC ile haberleşir**
  - **Python CLI arayüzü ile kontrol edilebilir**

## Proje İçeriği:
  Dosya	Açıklama
  - mplab_mpsam_uyumlu_asm.txt -> PIC16F877A için Assembly firmware
  - Python_Serial_Interface.py ->	PC tarafı Python seri haberleşme arayüzü
  
## Sistem Özellikleri:
  - Mikrodenetleyici (PIC16F877A)
  - ADC ile sıcaklık ölçümü
  - Keypad ile sıcaklık girişi
  - 4 haneli 7-segment display kontrolü
  - UART (9600 baud) haberleşme
  - Fan RPM ölçümü (TMR0 ile)
  - Isıtıcı / soğutucu LED kontrolü
  - Kullanıcı sıcaklık aralığı: 10.0°C – 50.0°C

## Python Arayüzü:
  - **COM port üzerinden bağlantı**
   Anlık olarak:
   - Ortam sıcaklığı
   - Hedef sıcaklık
   - Fan hızı
   - Kullanıcıdan hedef sıcaklık alma
   - Basit CLI menü sistemi

## Donanım Gereksinimleri:
  - PIC16F877A
  - 4x7 Segment Display
  - 4x4 Keypad
  - Sıcaklık sensörü (ADC girişinde analog)
  - Fan + tach çıkışı
  - UART-TTL dönüştürücü (FTDI / CH340 / vs.)
  - MPLAB X + MPASM

## Proje Görselleri

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/099ab990-e500-4242-9d70-5237c2a0523c" />
<img width="400" height="350" alt="image" src="https://github.com/user-attachments/assets/b00826ff-c760-478d-abe1-d111a1b149fc" />

