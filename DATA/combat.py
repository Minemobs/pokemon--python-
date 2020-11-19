import pokemon2
import time
import os


def combat(name, rival, pokemonr, pokemon):
    os.system("cls")
    print("le combat commence !")
    time.sleep(2)
    print("{} sort un {}, vous sortez un {}".format(rival, pokemonr["name"], pokemon["name"]))
    time.sleep(3)
    combat = True
    while combat == True:
        action = input("quel action voulez vous faire ?\n\u001b[31m attaques 1 \u001b[0m   \u001b[34msac 2\u001b[0m\n")
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

def verifwinloose(pokemonr, pokemon):
    print("verif")
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
    print("{} a utiliser l'attaque {} et a fait {} points de dégats à {} donc il lui reste {} points de vie".format(pokemonr["name"], attaque["name"], attaque["attack_damage"], pokemon["name"], pokemon["pv"]))
    time.sleep(6)

def give_item(name, rival, pokemonr, pokemon):
    print("voici vos objets :")
    for x in range(0, len(pokemon2.invontory)):
        print(pokemon2.invontory[x]["name"] + " " + str(x))
    item = input("quel objet voulez vous utiliser ? (merci de mettre le nombre a coté de l'objet)\n")
    try:
        item = int(item)
    except:
        print("merci de rentrer un nombre valide !")
        return
    usepotion(name, rival, pokemonr, pokemon, item)
    

def usepotion(name, rival, pokemonr, pokemon, key):
    if pokemon["pv"] + pokemon2.invontory[key]["effet"] >= pokemon["pv_max"]:
        pokemon["pv"] = pokemon["pv_max"]
    else:
        pokemon["pv"] = pokemon["pv"] + pokemon2.invontory[key]["effet"]
    print("{} a récupéré {} pv(s) !".format(pokemon["name"], pokemon2.invontory[key]["effet"]))
    pokeattackr(name, rival, pokemonr, pokemon)