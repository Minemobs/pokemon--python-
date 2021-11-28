import combat
import pokemon2
import os
import console

console.clear()

running = True
name = input("professeur Chêne: Bonjours j'ai perdu ma fiche comment t'appelle tu deja ?\n")
if name == "DEBUG":
    pokemon2.invontory.append({"name": "potion", "effet": 10})
    result = combat.combat(name, "<adverse>", pokemon2.evoli, pokemon2.pikachu)
    if result == True:
        print("Bravo vous avez gagné !")
    if result == False:
        print("vous avez perdu :'(")
    if result == None:
        print('vous avez fuit, donc personne gagne...')
    exit()
import time
print("professeur Chêne: c'est un très bon nom {} ! D'ailleur je voudrais même te laisser choisir ton compagnion d'aventure... mais il n'en a plus, appart un c'est le seul qui nous reste il n'est pas pour les débutants comme toi donc attention".format(name))
time.sleep(float(8.50))
print("Tu a reçu un pikachu !")
time.sleep(3)
print("d'ailleur vu t'on pokemon pour t'aider voici une potion")
time.sleep(3)
print("tu a reçu une potion")
pokemon2.invontory[0] = {"name": "potion", "effet": 10}
time.sleep(2)
print("*quelqu'un entre*")
time.sleep(1.50)
print("?: bonjours Chêne comment va tu ?")
time.sleep(3)
print("prof. Chêne: sa va et toi ?")
time.sleep(3)
print("?: nickel")
time.sleep(2)
print("prof. Chêne: pendant que tu est la voudrais tu faire un combat contre {} ?".format(name))
time.sleep(4)
print("?: bien sûr")
time.sleep(2)
if combat.combat(name, "?", pokemon2.evoli, pokemon2.pikachu) == False:
    print("Bravo c'était un beau combat malheureusement tu n'a pas pu le réussir... mais tu peux encore tanter ta chance")
else:
    time.sleep(1.50)
    print("?: bravo {} au faite j'ai oublier de te le dire mais je m'appelle Regis\nmais je suis navrer de te le dire mais tu est dans une version bêta du jeu donc tu peux combatre tout les pokemons que tu veux ici mais il n'aura pas d'histoire malheureusement".format(name))
while running:
    pass