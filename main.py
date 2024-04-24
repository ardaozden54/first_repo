name_dict = {
      "CRİNGE":"Garip ya da utandırıcı bir şey",
      "LOL":"Komik bir şeye verilen cevap",
}
word = input("Anlamadığınız bir kelime yazın(hepsini büyük arfle): ")
if word in name_dict:
  meaning = meme_dict(word)
  print(f"{word} kelimesi şu anlama gelir: {meaning}")
else:
  print("bu kelimenin anlamını bilmiyorum.")
