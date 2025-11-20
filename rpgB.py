from random import randint


slots = [None] * 10
known_spells = ["ice","fireball","shield"]
all_spells = ["ice", "fireball", "shield", "spiked sheild", "energy draining touch", "elektra",
                    "bloody sacrifice", "bloody sword", "obsessive anxiety spell", "bloody meditation",
                    "touch of fading", "luck power", "aura enhancement", "aura of withering",
                    "aura of magic strengthening", "aura of magic cleansing"]
not_luck = -25
gold = 20

#0-hp 1-reg_man (demon damag) 2-mana (demon regen) 3-aura (demon stun) 4-passiw MagDamag (demon rezist stun)
invent=["Cup of Deep Water", "Dreams about Lightning", "Stone of the Unbreakable Shield", "Ashes of the Burnt Name"]
her0=[100,50,100,10,0]
death=[999,999,99,0,9]
imp=[60,12,40,-5,0]

wrath = [300, 40, 4, -2, 2]
bloodfiend = [180, 28, 3, -1, 1]
scarred_hound = [90, 16, 2, 0, 1]

envy = [330, 42, 5, -3, 3]
shade_demon = [200, 30, 3, -2, 2]
mimic = [170, 26, 2, -1, 2]

greed = [360, 48, 5, -3, 4]
horned_demon = [220, 32, 3, -2, 3]
treasure_golem = [200, 30, 2, -1, 3]

sloth = [400, 50, 6, -3, 5]
slothfiend = [240, 34, 3, -2, 3]
drowsy_wraith = [220, 32, 2, -1, 3]

gluttony = [450, 56, 6, -4, 6]
devouring_demon = [260, 36, 3, -3, 4]
gulper_fiend = [240, 34, 2, -2, 4]

pride = [500, 60, 7, -4, 7]
arrogant_demon = [300, 40, 3, -3, 4]
vainglorious_wraith = [260, 38, 2, -2, 4]

lust = [550, 70, 7, -5, 8]
succubus = [320, 44, 3, -3, 5]
incubus = [300, 42, 2, -2, 5]


def set_spell(known_spells):
      while True:
            print_slots()
            slot_number = input("What slot? (1-10, 0 = end): ")
            try:
                  slot_number = int(slot_number)
            except ValueError:
                continue
            if slot_number == 0:
                  print("End")
                  break
            elif 1<=slot_number<=10:
                  spell_name = input("Name of the spell:"
                                     f" (You know {known_spells}) ").strip()
                  if spell_name in known_spells:
                        slots[slot_number - 1] = spell_name
                  elif spell_name not in known_spells:
                        print("The Unknown Spell!")
      return()


def print_slots():
    print("\nSlots:")
    for i, spell in enumerate(slots, start=1):
        print(f"{i} - {spell if spell else '[None]'}")
    print()

#0-hp 1-reg_man (demon damag) 2-mana (demon regen) 3-aura (demon stun) 4-luck (demon rezist stun)

def war(enemy):
    global her0
    global inwent
    while True:
        aura = 0
        while enemy[0]>0 or her0[0]>0:
            print(enemy)
            print(her0)
            print("1 or another - skipping a turn, 2 - magic, 3 - item")
            inp=input()
            if inp=="1":
                if aura == 1:
                    enemy[0] -= her0[3]
                    her0[2] += her0[3] / 2
                elif aura == 2:
                    her0[0] += her0[3] / 2
                    her0[2] += her0[3] / 5
                elif aura == 3:
                    if her0[3] > 50:
                        her0[1] += 1
            elif inp=="2":
                inp = int(input("what spell do you want to use? 0 - final. Slot: \n"))
                use_spell = slots[inp - 1]
                if use_spell == "ice":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2]:
                        her0[2] -= mana
                        enemy[3] += round(mana / 5)
                elif use_spell == "fireball":
                    print(f"how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2]:
                        her0[2] -= mana
                        enemy[0] -= mana * 10
                elif use_spell == "sheild":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2]:
                        her0[2] -= mana
                    her0[0] += mana * 2
                elif use_spell == "spiked sheild":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2]:
                        her0[2] -= mana
                        enemy[0] -= mana / 2
                        her0[0] += mana
                elif use_spell == "energy draining touch":
                    mana = int(input())
                    if mana <= her0[2]:
                        her0[2] -= mana
                        enemy[0] -= mana
                        her0[0] += mana / 2
                elif use_spell == "elektra":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2]:
                        her0[2] -= mana
                        enemy[0] -= mana
                        enemy[3] = round(mana / 10)
                elif use_spell == "bloody sacrifice":
                    print("How much HP do you want to use?")
                    hp = int(input())
                    her0[0] -= hp
                    her0[2] += hp
                elif use_spell == "bloody sword":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    enemy[0] -= mana * 20
                    her0[0] -= round(mana / 5)
                elif use_spell == "obsessive anxiety spell":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if her0[2] >= mana >= 30:
                        her0[2] -= mana
                        enemy[4] -= 1
                elif use_spell == "bloody meditation":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2] and mana <= her0[0]:
                        her0[0] -= mana
                        her0[2] -= mana
                        her0[1] += round(mana / 50)
                elif use_spell == "touch of fading":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2] and mana <= her0[0]:
                        enemy[0] -= mana * 4
                        enemy[2] -= round(mana / 10)
                elif use_spell == "luck power":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2] and mana <= her0[0]:
                        her0[4] += mana / 12
                elif use_spell == "aura enhancement":
                    print("how much mana do you want to use?")
                    mana = int(input())
                    if mana <= her0[2] and mana <= her0[0]:
                        her0[3] += mana / 4
                elif use_spell == "aura of withering":
                    aura = 1
                elif use_spell == "aura of magic strengthening":
                    aura = 2
                elif use_spell == "aura of magic cleansing":
                    aura = 3
                elif inp == 0:
                    break
            if inp == "3":
                print(invent)
                print("Cup of Deep Water (mana + 80)", "Dreams about Lightning (stun enemy + 7)", "Stone of the Unbreakable Shield (hp + 120)", "Ashes of the Burnt Name (hp enemy - 70)")
                use = input("What do you want use? ")
                if use == "Deep Water" and "Deep Wather" in invent:
                    invent.remove("Deep Wather")
                    her0[2] += 80
                elif use == "Lightning Dreams" and "Lightning Dreams" in invent:
                    invent.remove("Lightning Dreams")
                    enemy[3] += 7
                elif use == "Shield Stone" and "Shield Stone" in invent:
                    invent.remove("Shield Stone")
                    her0[0] += 120
                elif use == "Fire Ashes" and "Fire Ashes" in invent:
                    invent.remove("Fire Ashes")
                    enemy[0] -= 70
            elif enemy[3] > 0:
                enemy[3] -= enemy[4]
                print("Enemy skips a turn")
            if enemy[0]<=0:
                print("Your opponent defeat.")
                break
            enemy[0] += enemy[2]
            if her0[0]<0:
                print("YOU DEAD")
                break
            if enemy[3] <= 0:
                ran = randint(not_luck, her0[4])
                if ran < 0:
                    if ran == not_luck:
                        print("critical failure")
                        her0[0] -= enemy[1] * 2
                    else:
                        her0[0] -= enemy[1]
                elif ran == her0[4]:
                    print("critical success")
                    enemy[0] -= enemy[1]
                else:
                    print("the enemy missed")
        if enemy[0] <= 0:
            break
        if her0[0] < 0:
            break



print("This isn't the story of your live. This is the story of your death. What's your name, Magus?")
player=input()
print(f"Hello {player}. And now your enemy will be your Death. It came during an experiment for immortality.... Because everyone knows that even Death can be defeated by Magic.\n You have a magic shield, meaning your HP {her0[0]}, Mana Regeneration {her0[1]}, Mana {her0[2]}, Aura {her0[3]}, and Luck {her0[4]}. {her0}.\n However, your opponents have HP {[imp[0]]}, damage {[imp[1]]}, regeneration {[imp[2]]}, stun {[imp[3]]} and stun resistance {[imp[4]]}. For example Imp: {imp}")

enemy = death
set_spell(known_spells)
war(enemy)

if her0[0] <= 0:
    level = 1
    print("\n\nBut it is not final. Its start. You feel fire instead of blood. You yourself have become a demon.")
    her0 = [100,50,100,10,13]
    if her0[0] < 0:
        print("\n 1 – Challenge the demon.\n"
              "2 – Wander around the area.\n"
              "3 – Go to the city you saw.\n")
        if level == 1:
            print("YOU ARE IN THE AREA OF THE FIRST DEMON'S RULE.\n"
                  "Demon Wrath.\n"
                  "Volcanic Wastes. A fiery landscape of molten rivers and erupting volcanoes, reflecting unbridled rage.")
        elif level == 2:
            print("YOU HAVE ENTERED THE DOMAIN OF ENVY.\n"
                  "Demon Envy.\n"
                  "Shattered Mirrors. A distorted realm of glassy ruins reflecting endless desire and jealousy.")
        elif level == 3:
            print("YOU STEP INTO THE TERRITORY OF GREED.\n"
                  "Demon Greed.\n"
                  "Golden Vaults. Mountains of treasure glint in dim light, tempting and trapping all who enter.")
        elif level == 4:
            print("YOU HAVE REACHED THE DOMAIN OF SLOTH.\n"
                  "Demon Sloth.\n"
                  "Forsaken Gardens. Overgrown and stagnant lands, where lethargy and decay reign supreme.")
        elif level == 5:
            print("YOU ENTER THE DOMAIN OF GLUTTONY.\n"
                  "Demon Gluttony.\n"
                  "Endless Banquet. A grotesque landscape of overflowing feasts and consumption without end.")
        elif level == 6:
            print("YOU STEP INTO THE DOMAIN OF PRIDE.\n"
                  "Demon Pride.\n"
                  "Crystal Spires. Towering, glittering structures reflecting vanity and arrogance in every angle.")
        elif level == 7:
            print("YOU ENTER THE DOMAIN OF LUST.\n"
                  "Demons Succubus and Incubus.\n"
                  "Scarlet Halls. A seductive and dangerous world of desire, temptation, and forbidden pleasures.")
        inp = input()
        if inp == input("1"):
            if level == 1:
                enemy = wrath
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            elif level == 2:
                enemy = envy
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            elif level == 3:
                enemy = greed
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            elif level == 4:
                enemy = sloth
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            elif level == 5:
                enemy = gluttony
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            elif level == 6:
                enemy = pride
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            if level == 7:
                enemy = lust
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            if level == 8:
                enemy = death
                war(enemy)
                if her0[0] > 0:
                    level += 1
                else:
                    print("YOU DIED")
        elif inp == input("2"):
            ran = randint(1,5)
            if ran == 1 or ran == 2 or ran == 3:
                ran_en = randint(1,3)
                if ran_en == 1:
                    enemy = imp
                if level == 1:
                    if ran_en == 2:
                        enemy = scarred_hound
                    elif ran_en == 3:
                        enemy = bloodfiend
                elif level == 2:
                    if ran_en == 2:
                        enemy = mimic
                    elif ran_en == 3:
                        enemy = shade_demon
                elif level == 3:
                    if ran_en == 2:
                        enemy = treasure_golem
                    elif ran_en == 3:
                        enemy = horned_demon
                elif level == 4:
                    if ran_en == 2:
                        enemy = drowsy_wraith
                    elif ran_en == 3:
                        enemy = slothfiend
                elif level == 5:
                    if ran_en == 2:
                        enemy = gulper_fiend
                    elif ran_en == 3:
                        enemy = devouring_demon
                elif level == 6:
                    if ran_en == 2:
                        enemy = vainglorious_wraith
                    elif ran_en == 3:
                        enemy = arrogant_demon
                elif level == 7:
                    if ran_en == 2:
                        enemy = incubus
                    elif ran_en == 3:
                        enemy = succubus
                print(f"The {enemy} meets you")
                war(enemy)
                if her0[0] > 0 and ran_en == 1:
                    gold += randint(0, 5)
                elif her0[0] > 0 and ran_en == 2:
                    gold += randint(1, 10)
                elif her0[0] > 0 and ran_en == 3:
                    gold += randint(5, 20)
                else:
                    print("YOU DIED.\n But there is no death in hell. You simply won't be able to defeat anyone until you regain your strength.")
            elif ran == 3:
                print("You find scattered gold coins")
                gold += randint(4, 44)
            elif ran == 4:
                print("You find a magic item in a chest standing in the middle of the road.")
                ran_en = randint(1,4)
                if ran_en == 1:
                    print("You find a dark spring")
                    invent.append("Deep Water")
                elif ran_en == 2:
                    print("You have come across a strange place where lightning flashes.")
                    invent.append("Lightning Dreams")
                elif ran_en == 3:
                    print("You find an altar in the shape of a shield with a stone on it/")
                    invent.append("Shield Stone")
                elif ran_en == 4:
                    print("You find a handful of smoldering ashes.")
                    invent.append("Fire Ashes")
        elif inp == input("3"):
            print("You meet an old friend, the robot V-42, a Necromechanic who once came to your world from hell. True, he disappeared five years ago. And now he's here."
                  "\n 1 - Rest in V-42's house."
                  "\n 2 - Enter the library."
                  "\n 3 - Enter the merchant's shop.")
            inp = input()
            if inp == 1:
                if level == 1:
                    her0 = [100, 50, 100, 10, 13]
                if level == 1:
                    her0 = [100, 50, 100, 10, 13]
                elif level == 2:
                    her0 = [120, 55, 110, 11, 14]
                elif level == 3:
                    her0 = [140, 60, 120, 12, 15]
                elif level == 4:
                    her0 = [160, 65, 130, 13, 16]
                elif level == 5:
                    her0 = [180, 70, 140, 14, 17]
                elif level == 6:
                    her0 = [200, 75, 150, 15, 18]
                elif level == 7:
                    her0 = [220, 80, 160, 16, 19]
            elif inp == 2:
                print(set(all_spells) - set(known_spells))
            elif inp == 3:
                print("What do you want to buy?\n"
                      "1 - Deep Water (20 gold)\n"
                      "2 - Lightning Dreams (35 gold)\n"
                      "3 - Shield Stone (25 gold)\n"
                      "4 - Fire Ashes (30 gold)")
                inp = input()
                if inp == 1 and gold >= 20:
                    gold -= 20
                    invent.append("Deep Water")
                elif inp == 2 and gold >= 35:
                    gold -= 35
                    invent.append("Lightning Dreams")
                elif inp == 3 and gold >= 25:
                    gold -= 25
                    invent.append("Shield Stone")
                elif inp == 4 and gold >= 30:
                    gold -= 30
                    invent.append("Fire Ashes")




                # "Deep Water (mana + 80)", "Lightning Dreams (stun enemy + 7)", "Shield Stone (hp + 120)", "Fire Ashes (hp enemy - 70)"


else:
    print("Bedziesz zyl wiecznie. Czy to jest dobry koniec czy zly?")