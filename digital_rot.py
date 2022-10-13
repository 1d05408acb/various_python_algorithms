def digital_rot(n):
    d = len(str(n)) # Bruker len på å sjekke lengden på strengen (4 tall dette tilfellet)
    while d > 1:
        n = sum(int(k) for k in str(n)) # Dette regnet ut summen av tallene (altså tverrsummen)
        print(n) # Printer ut tverrsummen
        d = len(str(n)) # Sjekker lengden på tverrsummen
    print("Digital rot er: " + str(n)) # Printer ut digital rot

tall = input("Skriv inn tallet du vil finne digital rot på: ")
digital_rot(tall)