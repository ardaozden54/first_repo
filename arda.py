import random

karakterler = "_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    sayi = int(input("Kaç karakterden oluşan bir şifre istersin?"))
    parola = ""
    for i in range(sayi):
            parola += random.choice(karakterler)
    print("Oluşturulan şifre:", parola)
