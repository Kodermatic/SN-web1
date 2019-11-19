print ("Kako se počutiš danes?")
pocutje = input ("Srečno, živčno, žalostno, vznemirljivo, umirjeno?: " ).lower().strip()

if pocutje == "srečno":
  print("Super te je videti srečnega!")
elif pocutje == "živčno":
  print("Vdihni izdihni, vdihni izdihni, vdihni izdihni. Že izgledaš bolje!")
elif pocutje  == "žalostno":
  print("Tukaj imaš robček, glavo gor!")
elif pocutje  == "vznemirljivo":
  print("Zakaj si čisto na trnjih? Malo še počakaj pa bo vsega konec.")
elif pocutje  == "umirjeno":
  print("Zbudi se iz te svoje nirvane!")
else:
  print("Ne razumem?")