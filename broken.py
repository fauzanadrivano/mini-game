allheroes = [{"Hero" : "Kagura", "Role" : "Mage", "DMG" : 350, "Gold" : 1000},
             {"Hero" : "Yve", "Role" : "Mage", "DMG" : 250, "Gold" : 1000},
             {"Hero" : "Lancelot", "Role" : "Assassin", "DMG" : 200, "Gold" : 1000},
             {"Hero" : "Hayabusa", "Role" : "Assassin", "DMG" : 300, "Gold" : 1000},
             {"Hero" : "Natalia", "Role" : "Assassin", "DMG" : 150, "Gold" : 1000},
             {"Hero" : "Cecilion", "Role" : "Mage", "DMG" : 200, "Gold" : 1000}]

magic = [{"Name" : "Necklace of Durance", "DMG" : 50, "Price" : 250},
         {"Name" : "Lightning Truncheon", "DMG" : 100, "Price" : 300},
         {"Name" : "Blood Wings", "DMG" : 300, "Price" : 500}]

attack = [{"Name" : "War Axe", "DMG" : 100, "Price" : 250},
         {"Name" : "Endless Battle", "DMG" : 300, "Price" : 400},
         {"Name" : "Blade of Despair", "DMG" : 400, "Price" : 700}]

spell = [{"Name" : "Execute", "DMG": 300},
         {"Name" : "Flameshot", "DMG": 200}]


def chooseHero():
  print("Select 1 Hero you want to play: ")
  selectedhero = {}
  for i in range(len(allheroes)):
    print("Id : {}".format(i))
    print("Detail : {}".format(allheroes[i]))
  inputs = input("silahkan masukkan pilihan Id: ")
  try:
    selectedhero.update(allheroes[int(inputs)])
    return selectedhero
  except:
    return "Wrong Input!"

def chooseSpell(hero):
  selectedhero = hero
  print("\n{} - DMG {}\n".format(selectedhero["Hero"],selectedhero["DMG"]))
  for i in range(len(spell)):
      print("Id: {} : {} - DMG {}".format(i,spell[i]["Name"], spell[i]["DMG"]))
  inputs = input("Pilih Id spell yang akan dipakai? ")
  selectedhero["Spell"] = spell[int(inputs)]
  print("\n{} - DMG {} - Spell {}\n".
        format(selectedhero["Hero"],selectedhero["DMG"],selectedhero["Spell"]))
  return selectedhero

def buyItem(hero):
  selectedhero = hero
  print("\n{} - DMG {} - Gold {}\n".
        format(selectedhero["Hero"],selectedhero["DMG"],selectedhero["Gold"]))
  if selectedhero["Role"] == "Mage":
    for i in range(len(magic)):
      print("Id: {} : {} - DMG {} - Price {}".
            format(i, magic[i]["Name"], magic[i]["DMG"], magic[i]["Price"]))
    inputs = input("silahkan masukkan pilihan Id: ")
    try:
      if selectedhero["Gold"] < magic[int(inputs)]["Price"]:
        print("Gold not enough")
        return selectedhero
      else:
        selectedhero["DMG"] += magic[int(inputs)]["DMG"]
        selectedhero["Gold"] -= magic[int(inputs)]["Price"]
        print("\nBUYING SUCCESS")
        print("\n{} - DMG {} - Gold {}\n".
              format(selectedhero["Hero"],selectedhero["DMG"],selectedhero["Gold"]))
    except:
      return "Wrong Input!"
  elif selectedhero["Role"] == "Assassin":
    for i in range(len(attack)):
      print("Id: {} : {} - DMG {} - Price {}".
            format(i, attack[i]["Name"], attack[i]["DMG"], attack[i]["Price"]))
    inputs = input("silahkan masukkan pilihan Id: ")
    try:
      if selectedhero["Gold"] < attack[int(inputs)]["Price"]:
        print("Gold not enough")
        return selectedhero
      else:
        selectedhero["DMG"] += attack[int(inputs)]["DMG"]
        selectedhero["Gold"] -= attack[int(inputs)]["Price"]
        print("\nBUYING SUCCESS")
        print("\n{} - DMG {} - Gold {}".
              format(selectedhero["Hero"],selectedhero["DMG"],selectedhero["Gold"]))
    except:
      return "Wrong Input!"
  if selectedhero["Gold"] < 250:
    return selectedhero
  else:
    inputt = input("Ingin beli lagi? (y/n)")
    if inputt == "y" or inputt == "Y":
      buyItem(selectedhero)
      return selectedhero
    else:
      return selectedhero

def fightLord(hero):
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
      print("Challange Success\n")

def start():
  print("Welcome to mini Mobile Legends Game\n\n")
  hero = chooseHero()
  selectedherospell = chooseSpell(hero)
  flag = True
  while flag:
    print("Select the activity you want to do:")
    print("1. Check Hero")
    print("2. Buy Item")
    print("3. Fight Lord")
    print("4. Exit")
    inputs = input("Choose the number :) ")
    if inputs == "1":
      print("{} - {} - DMG {} - Spell {}".
            format(selectedherospell["Hero"], selectedherospell["Role"], 
                  selectedherospell["DMG"], selectedherospell["Spell"]))
    elif inputs == "2":
      selectedherospell = buyItem(selectedherospell)
    elif inputs == "3":
      fightLord(selectedherospell)
    elif inputs == "4":
      print("Thank you for playing this game")
      flag = False
    else:
      return "Wrong Input"  