import pokemon_id
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
            if pokemon["attack_count"] == 1:
                actio1 = input("vous avez {} attaque au total\n\n- {} 1\n".format(pokemon["attack_count"], pokemon["attack"][0]["name"]))
                if actio1 == "1":
                    pokemonr["pv"] = pokemonr["pv"] - \
                        pokemon["attack"][0]["attack_damage"]
                    print("Bravo ! - {} pv à {} qui est donc à {} pv !".format(pokemon["attack"][0]["attack_damage"], pokemonr["name"], pokemonr["pv"]))
                    if pokeattackr(name, rival, pokemonr, pokemon) == False:
                        combat = False
                        return False

                    else:
                        print("c'est super effectif")
                        time.sleep(1.50)
                        print("vous avez gagner !")
                        combat = False
                        time.sleep(2)
                        os.system("cls")
                        return True
            if pokemon["attack_count"] == 2:
                actio2 = input("vous avez {} attaques au total\n\n- {} 1\n- {} 2\n".format(pokemon["attack_count"], pokemon["attack"][0]["name"], pokemon["attack"][1]["name"]))
                if actio2 == "1":
                    if pokemonr["pv"] - pokemon["attack"][0]["attack_damage"] >= 1:
                        pokemonr["pv"] = pokemonr["pv"] - pokemon["attack"][0]["attack_damage"]
                        print("Bravo ! - {} pv à {} qui est donc à {} pv !".format(
                            pokemon["attack"][0]["attack_damage"], pokemonr["name"], pokemonr["pv"]))
                        if pokeattackr(name, rival, pokemonr, pokemon) == False:
                            combat = False
                            return False


                    else:
                        print("c'est super effectif")
                        time.sleep(1.50)
                        print("vous avez gagner !")
                        combat = False
                        time.sleep(2)
                        os.system("cls")
                        return True
                if actio2 == "2":
                    if pokemonr["pv"] - pokemon["attack"][1]["attack_damage"] >= 1:
                        pokemonr["pv"] = pokemonr["pv"] - \
                            pokemon["attack"][1]["attack_damage"]
                        print("Bravo ! - {} pv à {} qui est donc à {} pv !".format(
                            pokemon["attack"][1]["attack_damage"], pokemonr["name"], pokemonr["pv"]))
                        if pokeattackr(name, rival, pokemonr, pokemon) == False:
                            combat = False
                            return False

                    else:
                        print("c'est super effectif")
                        time.sleep(1.50)
                        print("vous avez gagner !")
                        combat = False
                        time.sleep(2)
                        os.system("cls")
                        return True
        if action == "2":
            give_item(name, rival, pokemonr, pokemon)


def pokeattackr(name, rival, pokemonr, pokemon):
    time.sleep(2)
    print("au tours de {} !".format(pokemonr["name"]))
    import random
    attaque = pokemonr["attack"][random.randint(0, pokemonr["attack_count"] - 1)]
    if pokemon["pv"] - attaque["attack_damage"] >= 1:
        time.sleep(3)
        pokemon["pv"] = pokemon["pv"] - attaque["attack_damage"]
        print("{} a utiliser l'attaque {} et a fait {} points de dégats à {} donc il lui reste {} points de vie".format(pokemonr["name"], attaque["name"], attaque["attack_damage"], pokemon["name"], pokemon["pv"]))
        time.sleep(6)
        return True
    else:
        pokemon["pv"] = pokemon["pv_max"]
        pokemonr["pv"] = pokemonr["pv_max"]
        print("vous avez perdu mais vous re-tanterais la prochaine fois !")
        return False
        

def give_item(name, rival, pokemonr, pokemon):
    print("voici vos objets :")
    for x in range(0, len(pokemon_id.invontory)):
        print(pokemon_id.invontory[x]["name"] + " " + str(x))
    item = input("quel objet voulez vous utiliser ? (merci de mettre le nombre a coté de l'objet)\n")
    try:
        item = int(item)
    except:
        print("merci de rentrer un nombre valide !")
        return
    usepotion(name, rival, pokemonr, pokemon, item)
    

def usepotion(name, rival, pokemonr, pokemon, key):
    if pokemon["pv"] + pokemon_id.invontory[key]["effet"] >= pokemon["pv_max"]:
        pokemon["pv"] = pokemon["pv_max"]
    else:
        pokemon["pv"] = pokemon["pv"] + pokemon_id.invontory[key]["effet"]
    print("{} a récupéré {} pv(s) !".format(pokemon["name"], pokemon_id.invontory[key]["effet"]))
    pokeattackr(name, rival, pokemonr, pokemon)