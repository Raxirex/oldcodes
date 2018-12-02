import time
import getpass
azx = 1  #uyuşmsazlık olma durumu break komutu olmadan yazılması için
a = "   Özel karakterler şifre için uygun değildir."
dil = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
while azx == 1:
    setcipher = getpass.getpass(prompt='    Belirlemek istediğiniz şifre ', stream=None)
    cipherkey = getpass.getpass(prompt='    Lütfen şifreyi tekrar giriniz ', stream=None)
    addogru = input("Adınızı giriniz:   ")
    azx = 2
    for turkcekarakter in cipherkey:
        if turkcekarakter not in dil:
         print(a)
         azx = 1
    if str(setcipher) != str(cipherkey):
        print("Girdiğiniz şifreler uyuşmamaktadır. Lütfen tekrar giriniz.")
        azx = 1
hayir = {"Hayır","h","H","hayır"}
evet = {"evet","Evet","e","E"}
while azx ==2:
    time.sleep(0.1)
    print(" Yükleniyor...")
    time.sleep(2)
    print(" Şifre çözülüyor...")
    time.sleep(2)
    print("         Sisteme Giriş Yapınız")
    ad = input("    Adınızı giriniz     ")
    sifre = getpass.getpass(prompt='    Şifrenizi giriniz ', stream=None)
    cipherkey = str(cipherkey)
    addogru = str(addogru)
    if ad != (addogru):
        print(" Adınıza kayıtlı bir hesap bulunmamaktadır.")
        if sifre != (cipherkey):
            print(" Sifreniz Yanlış Giriş Yapamazsınız")
    else:
        print(" Merhaba  ", ad, " özel kodunuz (X650-O).")
    print(" Başka bir şey yapmak ister misiniz? evet/hayır ")
    e = input(" ")
    if e in evet:
        print("Nothing for now  ")
    elif e in hayir:
        break
time.sleep(10)
