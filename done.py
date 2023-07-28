heroes = [
    {"Hero": "Kagura", "Role": "Mage", "DMG": 350, "Gold": 1000},
    {"Hero": "Yve", "Role": "Mage", "DMG": 250, "Gold": 1000},
    {"Hero": "Lancelot", "Role": "Assassin", "DMG": 200, "Gold": 1000},
    {"Hero": "Hayabusa", "Role": "Assassin", "DMG": 300, "Gold": 1000},
    {"Hero": "Natalia", "Role": "Assassin", "DMG": 150, "Gold": 1000},
    {"Hero": "Cecilion", "Role": "Mage", "DMG": 200, "Gold": 1000}
]

sihir = [
    {"Name": "Necklace of Durance", "DMG": 50, "Price": 250},
    {"Name": "Lightning Truncheon", "DMG": 100, "Price": 300},
    {"Name": "Blood Wings", "DMG": 300, "Price": 500}
]

serangan = [
    {"Name": "War Axe", "DMG": 100, "Price": 250},
    {"Name": "Endless Battle", "DMG": 300, "Price": 400},
    {"Name": "Blade of Despair", "DMG": 400, "Price": 700}
]

mantra = [
    {"Name": "Execute", "DMG": 300},
    {"Name": "Flameshot", "DMG": 200}
]


def printList(i, list, tipe):
    if i == len(list):
        return
    else:
        if tipe == 'hero':
            print("Id : {}".format(i))
            print("Detail : {}".format(list[i]))
        elif tipe == 'mantra':
            print("Id: {} : {} - DMG {}".format(i, list[i]["Name"], list[i]["DMG"]))
        elif tipe == 'item':
            print("Id: {} : {} - DMG {} - Price {}".format(i, list[i]["Name"], list[i]["DMG"], list[i]["Price"]))

        return printList(i + 1, list, tipe)


def pilihHero(allheroes):
    print("Select 1 Hero you want to play: ")
    selectedhero = {}

    printList(0, allheroes, 'hero')

    inputs = input("\nSilakan masukkan pilihan Id: ")
    try:
        selectedhero.update(allheroes[int(inputs)])
        return selectedhero
    except:
        return "Wrong Input!"


def pilihMantra(hero, spell):
    selectedhero = hero
    print("\n{} - DMG {}\n".format(selectedhero["Hero"], selectedhero["DMG"]))

    printList(0, spell, 'mantra')

    inputs = input("\nPilih Id spell yang akan dipakai: ")
    selectedhero["Spell"] = spell[int(inputs)]
    print("\n{} - DMG {} - Spell {}".format(selectedhero["Hero"], selectedhero["DMG"], selectedhero["Spell"]))

    return selectedhero


def beli_item(hero):
    selectedhero = hero
    print("\n{} - DMG {} - Gold {}\n".format(selectedhero["Hero"], selectedhero["DMG"], selectedhero["Gold"]))

    def itembyrole(item):
        printList(0, item, 'item')

        inputs = input("silakan masukkan pilihan Id : ")
        try:
            if selectedhero["Gold"] < item[int(inputs)]["Price"]:
                print("Gold not enough")
                return selectedhero
            else:
                selectedhero["DMG"] += item[int(inputs)]["DMG"]
                selectedhero["Gold"] -= item[int(inputs)]["Price"]
                print("\nBUYING SUCCESS")
                print("\n{} - DMG {} - Gold {}\n".format(selectedhero["Hero"], selectedhero["DMG"], selectedhero["Gold"]))

                if selectedhero["Gold"] < 250:
                    return selectedhero
                else:
                    inputt = input("Ingin beli lagi? (y/n) : ")
                    if inputt == "y" or inputt == "Y":
                        beli_item(hero)(item)
                        return selectedhero
                    else:
                        return selectedhero
        except:
            return "Wrong Input!"

    return itembyrole


def bertarung(hero):
    lord = 1000
    selectedhero = hero
    spell = selectedhero["Spell"]
    print("Fight Begin\n")
    print("Lord - HP: {}\n".format(lord))
    while lord > 0:
        print("0 || {} - DMG {}".format(selectedhero["Hero"], selectedhero["DMG"]))
        print("1 || {} - DMG {}".format(spell["Name"], spell["DMG"]))
        fight = input("Select 0 to fight with hero DMG or 1 to fight with Spell DMG: ")
        if fight == "0":
            lord -= selectedhero["DMG"]
        elif fight == "1":
            lord -= spell["DMG"]
        else:
            print("Wrong Input!")

        if lord > 0:
            print("\nLord - HP: {}\n".format(lord))
        else:
            lord = 0
            print("\nLord - HP: {}\n".format(lord))
            print("Challenge Success\n")


def main():
    print("Welcome to mini Mobile Legends Game\n\n")
    try:
        hero = pilihHero(heroes)
        selectedherospell = pilihMantra(hero, mantra)
    except:
        print("Wrong Input !!!\n")
        main()
    flag = True
    while flag:
        print("\nSelect the activity you want to do:")
        print("1. Check Hero")
        print("2. Buy Item")
        print("3. Fight Lord")
        print("4. Exit")
        inputs = input("Choose the number : ")
        if inputs == "1":
            print("{} - {} - DMG {} - Spell {}".format(selectedherospell["Hero"], selectedherospell["Role"],selectedherospell["DMG"], selectedherospell["Spell"]))
        elif inputs == "2":
            if selectedherospell["Role"] == "Mage":
                selectedherospell = beli_item(selectedherospell)(sihir)
            elif selectedherospell["Role"] == "Assassin":
                selectedherospell = beli_item(selectedherospell)(serangan)
        elif inputs == "3":
            bertarung(selectedherospell)
        elif inputs == "4":
            print("Thank you for playing this game")
            flag = False
        else:
            return "Wrong Input"


x = input('Main Game ? (y/n)\n')
if x == "y" or x == "Y":
    main()
else:
    print('Hallo dek !!!')
    exit()