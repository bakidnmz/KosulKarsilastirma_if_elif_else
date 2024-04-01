print(3 < 5)  # doğru bir ifade old için True sonucu üretir < ifadesi küçüktür anlamındadır.
print(3 > 5)  # yanlış bir ifade old için False sonucu üretir > ifadesi büyüktür anlamındadır.
print(7 <= 7)  # doğru bir ifade old için True sonucu üretir <= ifadesi küçükeşittir anlamındadır.
print(7 >= 7)  # doğru bir ifade old için True sonucu üretir >= ifadesi büyükeşittir anlamındadır.
print(8 >= 7)  # doğru bir ifade old için True sonucu üretir >= ifadesi büyükeşittir anlamındadır.
print(6 >= 7)  # yanlış bir ifade old için False sonucu üretir >= ifadesi büyükeşittir anlamındadır.
print(8 == 8)  # doğru bir ifade old için True sonucu üretir == ifadesi eşit midir anlamındadır.
print(7 != 8)  # doğru bir ifade old için True sonucu üretir != ifadesi eşit değil midir anlamındadır.
print((3 < 5) and (8 >= 7))  # and ile verilen ifadelerin hepsi doğruysa True en az biri yanlışsa False sonucu alınır.
print((3 < 5) and (8 == 7) and (13 == 21))  # son ifade yanlış old için False sonucu üretti.
print((3 < 5) or (8 >= 25))  # or ile verilen ifadeler içinde en az bir doğru varsa True Sonucu üretilir.
print((3 > 5) or (8 >= 25) or (13 == 21))  # False sonucu üretir çünkü tüm ifadeler yanlıştır.
print(not (4 < 9))  # not ile ters sonuç çıktısı alınır. 4<9 ifadesi doğru olmasına rağmen False üretir.
# İki Sayıyı Karşılaştırma Kodu
a = int(input("İlk Sayıyı Giriniz : "))  # kullanıcıdan ilk sayı alınıp int e dönüştürülür.
b = int(input("İkinci Sayıyı Giriniz : "))  # kullanıcıdan ikinci sayı alınıp int e dönüştürülür.
if a < b:  # karşılaştırma yapılıyor
    print(f"{a} sayısı {b} sayısından küçüktür.")
elif a == b:  # eşitlik durumu ayrılıyor
    print(f"{a} sayısı {b} sayısına eşittir.")
else:  # if ve elif koşulları yanlışsa ne yapılacağı belirleniyor
    print(f"{a} sayısı {b} sayısından büyüktür.")
