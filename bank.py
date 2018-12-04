f = open ('saldo.txt', 'r+')

print("*** Vällkommen till din bank ***")
#print är när man vill bara få ut ord i terminalen
saldo = 0
insattning = 0
uttag = 0
meny = 0
#=0 gör så att en string blir en variabel
while meny != 5:
    #while är en loop så om man skriver in en 4 så avslutar loopen 
    print("1. Visa slado")
    print("2. Uttag")
    print("3. Insättning")
    print("4. Spara")
    print("5. Avsluta")

    #try försöker köra koden nedan och hitta fel
    try:
        meny = int(input("Gör ett val "))
        
    #except gör så att programet inte crashar när du anger något annat än en siffra 
    except:
        print("Du måste ange en siffra!")
        

    try:
        #if du får ut det här när du skriver det som behövs 
        #elif i samma kod får du ut nått annat när du skriver nått annat korekt 
        #else om du inte skriver nått giltigt så händer det här 
        if meny == 3:
            insattning = input("Ange en siffra ") 
            saldo = saldo + int(insattning)
        elif meny == 2:
            uttag = input("Ange det du är skyldig ")
            saldo = saldo - int(uttag)
        elif meny == 1:
            print("Din saldo:" ,saldo)
        elif meny == 4:
            f.open
            f.write saldo
        elif meny == 5:
            print("Vällkommen åter")
        else:
            print("Du gjorde inte ett korrekt val! ")

    except:
        print("Du måste ange en siffra!")