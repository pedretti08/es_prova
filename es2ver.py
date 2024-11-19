media=int(input("scrivi la tua media dei voti"))
anno=int(input("scrivi in che hanno scolastico sei(3/4/5)"))
if(media==6):
    if (anno==3):
        print(f"il credito sarà 7-8")
    elif(anno==4):
        print(f"il credito sarà 8-9")
    else:
        print(f"il credito sarà 9-10")
elif(6<media<=7):
    if(anno==3):
        print(f"il credito sarà 8-9")
    elif(anno==4):
        print(f"il credito sarà 9-10")
    else:
        print(f"il credito sarà 10-11")
elif(7<media<=8):
    if(anno==3):
        print(f"il credito sarà 9-10")
    elif(anno==4):
        print(f"il credito sarà 10-11")
    else:
        print(f"il credito sarà 11-12")
elif(8<media<=8):
    if(anno==3):
        print(f"il credito sarà 10-11")
    elif(anno==4):
        print(f"il credito sarà 11-12")
    else:
        print(f"il credito sarà 12-13")
elif(9<media<=10):
    if(anno==3):
        print(f"il credito sarà 11-12")
    elif(anno==4):
        print(f"il credito sarà 12-13")
    else:
        print(f"il credito sarà 13-14")
else :
    print(f"hai sbagliato qualcosa")