BLACK = '\33[30m'
RED = '\33[31m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
BLUE = '\33[34m'
VIOLET = '\33[35m'
BEIGE = '\33[36m'
WHITE = '\33[37m'


def clasificar():
    frase = input("Frase?: ")
    lletra = frase.split()
    fraseNova = ""
    for y in frase:
        match y:
            case "A"|"a"|"á"|"Á"|"à"|"À"|"e"|"E"|"É"|"é"|"è"|"È"|"O"|"o"|"ó"|"ò"|"Ó"|"Ò"|"Ú"|"Ù"|"U"|"u"|"ú"|"ù"|"i"|"I"|"Í"|"í"|"ì"|"Ì" : fraseNova+= '\33[32m'+y
            case _: fraseNova+= '\33[30m'+y
    print(fraseNova)