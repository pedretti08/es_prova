lancio1=int(input("inserisci la lunghezza del primo lancio(0=nullo)"))
lancio2=int(input("inserisci la lunghezza del secondo lancio(0=nullo)"))
lancio3=int(input("inserisci la lunghezza del terzo lancio(0=nullo)"))
lancio4=int(input("inserisci la lunghezza del quarto lancio(0=nullo)"))
lancio5=int(input("inserisci la lunghezza del quinto lancio(0=nullo)"))
conto=0
media=0
if (lancio1!=0):
    media=media+lancio1
    conto=conto+1
if (lancio2!=0):
   media=media+lancio2
   conto=conto+1
if (lancio3!=0):
    media=media+lancio3
    conto=conto+1
if(lancio4!=0):
    media=media+lancio4
    conto=conto+1
if(lancio5!=0):
    media=media+lancio5
    conto=conto+1
if(conto==0):
    print(f"ci sono stati dei lanci nulli")
else :
    media=media/conto
    print(f"la media è di {media}")




