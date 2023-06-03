def prostokat(bok_a , bok_b):
  pole = bok_a*bok_b
  obwod = bok_a*2+bok_b*2
  return pole,obwod

print("Pole wynosi i obwod wynosza: " + str(prostokat(1,2)))

def kwadrat(bok):
  pole = bok^2
  obwod = bok*4
  return pole,obwod

print("Pole wynosi i obwod wynosza: " + str(kwadrat(4)))