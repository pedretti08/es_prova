fascine=5
scacchi=20
bancali=50
spesetrasporto=3
costokg=0.8
numerofascine=int(input("quante fascine hai preso? "))
numeroscacchi=int(input("quanti scacchi hai preso? "))
numerobancali=int(input("quanti bancali hai preso? "))
pesotot=(numerofascine*fascine)+(numeroscacchi*scacchi)+(numerobancali*bancali)
print(f"in totale hai preso {pesotot}kg di legna")
nosconto=costokg*pesotot
print(f"il prezzo senza sconto è di {nosconto}€")
print(f"il prezzo di trasporto è di {spesetrasporto}€")
if (pesotot>100):
  sconto=nosconto/100*15
else:
  sconto=0
prezzotot=nosconto-sconto+spesetrasporto
print(f"il prezzo finale su scontrino è di {round(prezzotot,2)}€ ")