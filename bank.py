print("*** Vällkommen till din bank ***")
saldo = 0
insattning = 0
uttag = 0
meny = 0
while meny != 4:
    print("1. Visa slado")
    print("2. Uttag")
    print("3. Insättning")
    print("4. Avsluta")

    try:
        meny = int(input("Gör ett val"))
    except:
        print("Du måste ange en siffra!")

    if meny == 3:
        insattning = input("Ange en siffra") 
        saldo = saldo + int(insattning)
    elif meny == 2:
        uttag = input("Ange det du är skyldig")
        saldo = saldo - int(uttag)
    elif meny == 1:
        print("Din saldo:" ,saldo)
    elif meny == 4:
        print("Vällkommen åter")
    else:
        print("Du gjorde inte ett korrekt val")
