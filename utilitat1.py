def contador():
    frase = ""
    vocals = []
    while frase != "\q":
        frase = input()
        res=[]
        lletres = ["a","b","c","d","e","f","g","h","j","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for x in range(len(frase)):
            contL=0
            for y in frase.lower():
                if y in lletres:
                    contL+=1
            conteo =f"Hi ha {contL} lletres"
            res.append(conteo)
        llista=list(set(res))
        print(llista)

