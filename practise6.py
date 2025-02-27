"""
def pocet_znaku():
    retezec = input("Zadej řetězec znaků: ")
    #pocet = pocet.count("")
  
    pocet = {}

    for letter in retezec(): 
        pocet.setdefault(letter, 0) 
        pocet[letter] += 1 

    print(pocet) 
"""
def pocet_znaku():
    pocet = 0
    text = input("Zadej řetězec znaků: ")
    letter_count = {}
    for letter in text.lower():
        letter_count.setdefault(letter, 0)  
        letter_count[letter] += 1
        pocet = pocet + 1
    print(pocet)

pocet_znaku()





def preskladani(seznam):
    seznam.reverse()
    return seznam

seznam = [4, 9, 6, 8, 7]
print(preskladani(seznam))


def nahrazeni(text):
    print(text)
    old = input("Co pujde pryc: ")
    future = input("Co tam budde: ")
    return text.replace(old, future)

ttt = "C je král"
print(nahrazeni(ttt))





USD = 22 #CZK
EUR = 25 #CZK
money = int(input("kolik máš k převodu:"))
vysledek_USD = money/USD
vysledek_EUR = money/EUR



def konvertor():
    money = int(input("kolik máš k převodu:"))
    vysledek_USD = money/USD
    vysledek_EUR = money/EUR
    return f"Máš {vysledek_USD} dolarů a {vysledek_EUR} euro"

print(konvertor())


def even_me():
    cislo = int(input("Zadej celé číslo:"))
    if(cislo % 2 == 0):
        return True
    else:
        return False

print(even_me())



cislo = int(input("Zadej číslo:"))

def number_walker(cislo):
    in range(1 - cislo)


def find_average():
    seznam = [1, 2, 90, 1998, -2]
    soucet = 0
    pocet = 1
    for number in seznam:
        soucet = soucet + number
        pocet = pocet + 1
        prumer = soucet/pocet
    return f"Průměr je {prumer}"

print(find_average())
