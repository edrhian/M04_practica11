"""
 Funció que donat un nom per l'usuari dins de la llista de noms, retorna un missatge, el qual es diferents per els diferents noms
 si no esta el nom en la llista, retorna un missatge avisant-ho.
"""
def nomRepMissatgeA():
    llistaNoms = ['Edrhian', 'Mustapha', 'Rosh', 'Eduardo', 'Juana']

    nomEscollit = input("Escriu un dels noms de la següent llista: {llistaNoms}: ".format(llistaNoms = llistaNoms))

    if(nomEscollit == llistaNoms[0]):
        print("Bon dia {nom0}".format(nom0 = llistaNoms[0]))
    elif (nomEscollit == llistaNoms[1]):
        print("Bona nit {nom1}".format(nom1=llistaNoms[1]))
    elif (nomEscollit == llistaNoms[2]):
        print("Bona tarda {nom2}".format(nom2=llistaNoms[2]))
    elif (nomEscollit == llistaNoms[3]):
        print("Salutacions, {nom3}".format(nom3=llistaNoms[3]))
    elif (nomEscollit == llistaNoms[4]):
        print("Hola {nom4}".format(nom4=llistaNoms[4]))
    else:
        print("El nom escrit no esta en la llista")

