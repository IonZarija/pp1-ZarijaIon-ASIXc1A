import utilitat1
import utilitat2
import utilitat3
import utilitat4

def menu(opcio):
    try:
        print("1. Signes puntuació - Quantitat\n" "2. Signes puntuació - Posició\n" "3. Text - Codificar\n" "4. Text - Descodificar\n" "5. Executar totes les utilitats\n" "6. Sortir de l'aplicació")
        opcio = int(input("Escull una opció: "))
        if opcio < 1 or opcio > 6:
            print("Opció incorrecta\n")
            opcio = menu(opcio)
        return opcio
    except:
        print("Introduce un número del menú\n")
        opcio = menu(opcio)

def get_utilitat(opcio):
    if opcio == 1:
        frase = utilitat1.contador()
        return frase
    elif opcio == 2:
        frase = utilitat2.cont()
        return frase
    elif opcio == 3:
        frase = utilitat3.traduccio()
        return frase
    elif opcio == 4:
        frase = utilitat4.clasificar()
        return frase
    elif opcio == 5:
        frase1 = utilitat1.contador()
        frase2 = utilitat2.cont()
        frase3 = utilitat3.traduccio()
        frase4 = utilitat4.clasificar()
    elif opcio == 6:
        print("Adeu")
