import pokemon2 as poke2
import time
import os
import console

pokemon2 = poke2

def combat(name, rival, pokemonr, pokemon):
    console.clear()
    print("le combat commence !")
    time.sleep(2)
    print("{} sort un {}, vous sortez un {}".format(rival, pokemonr["name"], pokemon["name"]))
    time.sleep(3)
    combat = True
    while combat:
        verif = verifwinloose(pokemonr, pokemon)
        if verif == "self_pokemon":
            return False
        if verif == "advers_pokemon":
            return True
        action = input("quel action voulez vous faire ?\n\u001b[31m attaques 1 \u001b[0m   \u001b[34msac 2\u001b[0m\n<placeholder> 3   fuir 4\n")
        if action == "1":
            time.sleep(1)
            print("liste des attaques :")
            for x in range(len(pokemon["attack"])):
                print(pokemon["attack"][x]["name"] + " " + str(x))
            attack = input("")
            try:
                attack = int(attack)
            except:
                print("nombre non valide re-éssayer")
                return
            pokemonr["pv"] = pokemonr["pv"] - pokemon["attack"][attack]["attack_damage"]
            if pokemon["pv"] <= 0 or pokemonr["pv"] <= 0:
                ret = verifwinloose(pokemonr, pokemon)
                if ret == "self_pokemon":
                    return False
                if ret == "advers_pokemon":
                    return True
            print("{} a perdu {} pv donc il lui en reste {} ! ".format(pokemonr["name"], pokemon["attack"][attack]["attack_damage"], pokemonr["pv"]))
            pokeattackr(name, rival, pokemonr, pokemon)

        if action == "2":
            give_item(name, rival, pokemonr, pokemon)
        verif = verifwinloose(pokemonr, pokemon)
        if verif == "self_pokemon":
            return False
        if verif == "advers_pokemon":
            return True

        import random
        if action == "4":
            time.sleep(2)
            chance = random.randint(1, 100)
            confirm = input("vous avez {}% de chance de fuir confirmez vous ? (Y/N)\n".format(chance))
            if confirm.upper() == "Y":
                chat = random.randint(1, 100)
                print(chat)
                if chat <= chance:
                    print("vous avez réussi a fuir !")
                    return None
                else:
                    print("vous n'avez pas pu fuir...")
                    pokeattackr(name, rival, pokemonr, pokemon)


def verifwinloose(pokemonr, pokemon):
    if pokemon["pv"] <= 0:
        return "self_pokemon"
    if pokemonr["pv"] <= 0:
        return "advers_pokemon"

def pokeattackr(name, rival, pokemonr, pokemon):
    time.sleep(2)
    print("au tours de {} !".format(pokemonr["name"]))
    import random
    attaque = pokemonr["attack"][random.randint(0, pokemonr["attack_count"] - 1)]
    time.sleep(3)
    pokemon["pv"] = pokemon["pv"] - attaque["attack_damage"]
    if pokemon["pv"] >= 1:
        print("{} a utiliser l'attaque {} et a fait {} points de dégats à {} donc il lui reste {} points de vie".format(pokemonr["name"], attaque["name"], attaque["attack_damage"], pokemon["name"], pokemon["pv"]))
    else:
        print("vous avez perdu !")
        return False
    time.sleep(6)

def give_item(name, rival, pokemonr, pokemon):
    print("voici vos objets :")
    for x in range(len(pokemon2.invontory)):
        print(pokemon2.invontory[x]["name"] + " " + str(x))
    item = input("quel objet voulez vous utiliser ? (merci de mettre le nombre a coté de l'objet)\n")
    try:
        item = int(item)
    except:
        print("merci de rentrer un nombre valide !")
        return
    usepotion(name, rival, pokemonr, pokemon, item)
    

def usepotion(name, rival, pokemonr, pokemon, item):
    try:
        if pokemon["pv"] + pokemon2.invontory[item]["effet"] >= pokemon["pv_max"]:
            pokemon["pv"] = pokemon["pv_max"]
        else:
            pokemon["pv"] = pokemon["pv"] + pokemon2.invontory[item]["effet"]
        print("{} a récupéré {} pv(s) !".format(pokemon["name"], pokemon2.invontory[item]["effet"]))
        del pokemon2.invontory[item]
        pokeattackr(name, rival, pokemonr, pokemon)
    except:
        print("merci de rentrer une valeur valide !")

result = combat("nom", "<adverse>", pokemon2.evoli, pokemon2.pikachu)
if result == True:
    print("Bravo vous avez gagné !")
if result == False:
    print("vous avez perdu :'(")
if result == None:
    print('vous avez fuit, donc personne gagne...')