voto1=int(input("scrivi il primo voto"))
voto2=int(input("scrivi il secondo numero"))
voto3=int(input("scrivi il terzo numero"))
mediafinale=input("vuoi che la media finale sia in trentesimi o in centesimi?")
media=(voto1+voto2+voto3)/3
if (mediafinale=="trentesimi"):
    print(f"la media esspressa in trentesimi è di {media}")
elif (mediafinale=="centesimi"):
    media1=(media)*100/30
    print(f"la media finale espressa in centesimi è di {(return(media1,2))}")
else:
    print(f"hai sbagliato qualcosa")
