"""

"""
def cont():
    frase=input("Frase?")
    lletres=frase.split()
    llis = []
    for x in range(len(frase)):
        cont=0
        pos=[]
        for y in frase:
            if y == frase[x]:
                cont+=1
                pos.append(x)
        conteo=f"Lletra: {frase[x]} | Quantitat: {cont} | Posició: {pos} | "
        llis.append(conteo)
    llista=list(set(llis))
    print(llista)